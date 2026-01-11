# 122. Best Time to Buy and Sell Stock II

## Problem Statement

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

Find and return the **maximum profit** you can achieve.

---

## Examples

### Example 1

**Input:** `prices = [7, 1, 5, 3, 6, 4]`  
**Output:** `7`  
**Explanation:** * Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = $5 - 1 = 4$.

* Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = $6 - 3 = 3$.
* **Total profit** is $4 + 3 = 7$.

### Example 2

**Input:** `prices = [1, 2, 3, 4, 5]`  
**Output:** `4`  
**Explanation:** * Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = $5 - 1 = 4$.

* **Total profit** is $4$.

### Example 3

**Input:** `prices = [7, 6, 4, 3, 1]`  
**Output:** `0`  
**Explanation:** * There is no way to make a positive profit, so we never buy the stock.

* **Total profit** is $0$.

---

## Constraints

* $1 \le prices.length \le 3 \times 10^4$
* $0 \le prices[i] \le 10^4$

---

## Logic & Strategy

The optimal approach for this problem is the **Greedy Algorithm**. Since we can perform as many transactions as we like, the maximum profit is the sum of every price increase between consecutive days.

1. **Iterate** through the price array starting from the second day (index 1).
2. **Compare** the current day's price with the previous day's price.
3. **If** the price today is higher than yesterday, add the difference to the total profit:
$$\text{Total Profit} = \sum_{i=1}^{n-1} \max(0, prices[i] - prices[i-1])$$
4. This captures every "upward slope" in the price graph, which mathematically results in the maximum possible profit.
