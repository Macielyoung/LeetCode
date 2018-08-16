## Problem

Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.

**Example 1:**

```
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
```

**Example 2:**

```
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
```

 

## Solution

* 动归。dp[i] = min(dp[i], dp[i-k**2]+1)。先减去一个完全平方数，用剩余数的dp值加1和原来的dp比较，谁小取谁。
* BFS。遍历所有相加情况，最先有0出现的情况即次数最少。