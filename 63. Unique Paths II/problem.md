## Problem

A robot is located at the top-left corner of a *m* x *n* grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

![img](https://leetcode.com/static/images/problemset/robot_maze.png)

An obstacle and empty space is marked as `1` and `0` respectively in the grid.

**Note:** *m* and *n* will be at most 100.

**Example 1:**

```
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
```



## Solution

* 动态规划

  ```
  dp[0][0] = 0, if s[0][0] = 1
  dp[0][0] = 1, if s[0][0] = 0
  
  dp[i][j] = 0, if s[i][j] = 1
  dp[i][j] = dp[i-1][j]+dp[i][j-1], if s[i][j] = 0
  return dp[-1][-1]
  ```