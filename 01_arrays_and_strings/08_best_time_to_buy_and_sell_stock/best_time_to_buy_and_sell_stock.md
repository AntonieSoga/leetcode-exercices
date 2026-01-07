# 121. Best Time to Buy and Sell Stock

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## Examples

### Example 1

**Input:** `prices = [7, 1, 5, 3, 6, 4]`  
**Output:** `5`  
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = $6 - 1 = 5$.  
*Note: Buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.*

### Example 2

**Input:** `prices = [7, 6, 4, 3, 1]`  
**Output:** `0`  
**Explanation:** In this case, no transactions are done and the max profit = 0.

---

## Constraints

* $1 \le \text{prices.length} \le 10^5$
* $0 \le \text{prices[i]} \le 10^4$

---

## Optimal Solution Logic (Sliding Window / One Pass)

To solve this in $O(n)$ time:

1. Initialize `min_price` to a very large value and `max_profit` to 0.
2. Iterate through the array:
    * Update `min_price` if the current price is lower than the current `min_price`.
    * Calculate the potential profit (current price - `min_price`).
    * Update `max_profit` if the potential profit is greater than the current `max_profit`.
3. Return `max_profit`.
