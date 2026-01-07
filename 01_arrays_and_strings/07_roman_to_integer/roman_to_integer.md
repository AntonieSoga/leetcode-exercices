# 13. Roman to Integer

## Symbol Mapping

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| :--- | :--- |
| **I** | 1 |
| **V** | 5 |
| **X** | 10 |
| **L** | 50 |
| **C** | 100 |
| **D** | 500 |
| **M** | 1000 |

---

## Problem Description

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five, we subtract it making four. The same principle applies to the number nine, which is written as `IX`.

There are **six instances** where subtraction is used:

* **I** can be placed before **V** (5) and **X** (10) to make 4 and 9.
* **X** can be placed before **L** (50) and **C** (100) to make 40 and 90.
* **C** can be placed before **D** (500) and **M** (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

---

## Examples

### Example 1

**Input:** `s = "III"`  
**Output:** `3`  
**Explanation:** `III = 3`.

### Example 2

**Input:** `s = "LVIII"`  
**Output:** `58`  
**Explanation:** `L = 50`, `V = 5`, `III = 3`.

### Example 3

**Input:** `s = "MCMXCIV"`  
**Output:** `1994`  
**Explanation:** `M = 1000`, `CM = 900`, `XC = 90`, and `IV = 4`.

---

## Constraints

* $1 \le \text{s.length} \le 15$
* `s` contains only the characters (`'I'`, `'V'`, `'X'`, `'L'`, `'C'`, `'D'`, `'M'`).
* It is guaranteed that `s` is a valid roman numeral in the range $[1, 3999]$.

---

## Solution Strategy

The core logic relies on comparing the current character's value with the next character's value:

1. Iterate through the string from left to right.
2. If the value of the **current** symbol is **less than** the value of the **next** symbol, subtract the current value from the total.
3. Otherwise, add the current value to the total.
