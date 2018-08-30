## Problem

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

**Example:**

```
Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```



## Solution

* 动态规划。

  ```
  f[i][j]表示正方形右下角可向左向上延伸的最大长度，需要比较三种case：
  1. f[i][j-1]中得到的最长边
  2. f[i-1][j]中得到的最长边
  3. f[i-1][j-1]中得到的最长边
  f[i][j] = min(f[i][j-1], f[i-1][j], f[i-1][j-1])+1
  answer : max(f[i][j])
  ```
