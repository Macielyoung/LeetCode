## Problem

Say you have an array for which the *i*th element is the price of a given stock on day *i*.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**

```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```

**Example 2:**

```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```



## Solution

* 开始想到的方法是把每个值对应的最大利润计算出来，然后求出最大的利润，然而时间复杂度太高了。
* 使用一个值记录最低价格，然后把当前价格和最低价格比较求利润，如果当前利润高于最大利润，则跟新最大利润，最终可得最大利润。