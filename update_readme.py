import os
import re
import requests
from datetime import datetime

# Configuration
README_FILE = "README.md"
EXCLUDE = {".git", ".vscode", ".github", "__pycache__"}
LEETCODE_API_URL = "https://leetcode.com/api/problems/all/"

def format_title(title_str):
    """Fixes Roman Numerals and applies proper title casing."""
    title = title_str.replace("-", " ").replace("_", " ").title()
    # Explicit mapping for Roman Numerals and acronyms
    fixes = {
        " Ii": " II",
        " Iii": " III",
        " Iv": " IV",
        " Vi": " VI",
        " Bst": " BST",
    }
    for wrong, right in fixes.items():
        if wrong in title:
            title = title.replace(wrong, right)
    return title

def fetch_leetcode_data():
    """Fetches problem metadata from LeetCode API."""
    print("☁️ Syncing with LeetCode API...")
    try:
        response = requests.get(LEETCODE_API_URL, timeout=15)
        if response.status_code == 200:
            data = response.json()
            return {
                p['stat']['question__title_slug']: {
                    "difficulty": ["Easy", "Medium", "Hard"][p['difficulty']['level'] - 1],
                    "id": p['stat']['frontend_question_id'],
                    "acceptance": round(p['stat']['total_acs'] / p['stat']['total_submitted'] * 100, 1),
                    "url": f"https://leetcode.com/problems/{p['stat']['question__title_slug']}/"
                }
                for p in data['stat_status_pairs']
            }
    except Exception as e:
        print(f"❌ API Error: {e}")
    return {}

def generate_readme():
    lc_metadata = fetch_leetcode_data()
    solutions_dict = {}

    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d not in EXCLUDE and not d.startswith('.')]
        for file in files:
            if file.endswith(".py") and file != "update_readme.py":
                full_path = os.path.join(root, file).replace("\\", "/")
                folder_path = os.path.dirname(full_path)
                
                if folder_path in solutions_dict: continue

                parts = root.split(os.sep)
                if len(parts) >= 3:
                    # '01_arrays_and_strings' -> 'Arrays & Strings'
                    category = format_title(parts[1].split("_", 1)[-1])
                    # Folder slug: '01_merge_sorted_array' -> 'merge-sorted-array'
                    slug = re.sub(r'^\d+_', '', parts[-1]).lower().replace("_", "-")
                else:
                    category = "General"
                    slug = file.replace(".py", "").replace("_", "-")

                meta = lc_metadata.get(slug, {"difficulty": "Unknown", "id": "?", "acceptance": 0, "url": "#"})

                solutions_dict[folder_path] = {
                    "category": category,
                    "title": format_title(slug),
                    "id": meta["id"],
                    "path": folder_path,
                    "difficulty": meta["difficulty"],
                    "acceptance": f"{meta['acceptance']}%",
                    "url": meta["url"]
                }

    solutions = sorted(list(solutions_dict.values()), key=lambda x: (x['category'], x['title']))
    stats = {"Easy": 0, "Medium": 0, "Hard": 0, "Unknown": 0}
    for s in solutions: stats[s['difficulty']] += 1

    targets = {"Easy": 50, "Medium": 50, "Hard": 20}

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    md_content = [
        "# 🐍 LeetCode Exercices",
        "",
        f"> **Last Synced:** `{now}` | **Total Solved:** `{len(solutions)}`",
        "",
        "## 📊 Progress Tracker",
        "",
        "| Category | Solved | Goal | Progress |",
        "| :--- | :---: | :---: | :--- |",
        f"| 🟢 **Easy** | {stats['Easy']} | {targets['Easy']} | ![Progress](https://geps.dev/progress/{int((stats['Easy']/targets['Easy'])*100)}) |",
        f"| 🟡 **Medium** | {stats['Medium']} | {targets['Medium']} | ![Progress](https://geps.dev/progress/{int((stats['Medium']/targets['Medium'])*100)}) |",
        f"| 🔴 **Hard** | {stats['Hard']} | {targets['Hard']} | ![Progress](https://geps.dev/progress/{int((stats['Hard']/targets['Hard'])*100)}) |",
        "",
        "---",
        "",
        "## 🚀 Solutions",
        "",
        "| # | Category | Problem | Solution | Difficulty | Acc % |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ]

    for s in solutions:
        diff_colors = {"Easy": "00b140", "Medium": "ffb800", "Hard": "ff2d55"}
        color = diff_colors.get(s['difficulty'], "lightgrey")
        diff_badge = f"![difficulty](https://img.shields.io/badge/-{s['difficulty']}-{color}?style=flat-square)"
        
        md_content.append(
            f"| {s['id']} | `{s['category']}` | [{s['title']}]({s['url']}) | [🐍 View]({s['path']}) | {diff_badge} | `{s['acceptance']}` |"
        )
    
    md_content.append("")
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(md_content))

    print(f"Dashboard generated with {len(solutions)} problems!")

if __name__ == "__main__":
    generate_readme()