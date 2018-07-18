## Problem

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

**Example:**

```
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
```



## Solution

* 开始想的是使用递归的方法，一步一步走到最后，把所有可能的情况求解出来，最后计算最小值，这种方法虽然可行，但是时间复杂度太高，会超时；

* 后来参考网上的解法，使用动态规划的同时，进行剪枝，每次计算最小值。

  `dp[i][j]` = min(`dp[i-1][j]` , `dp[i][j-1]`) + `grid[i][j]`