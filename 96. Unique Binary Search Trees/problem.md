## Problem

Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1 ... *n*?

**Example:**

```
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```



## Solution

* 卡特兰数（可以通过动态规划得出计算公式）

  总数应该是左子树个数乘以右子树个数，加上每个数都可以为根的情况

  ```
  dp[0] = 1 ,  dp[1] = 1
  dp[2] = dp[0] * dp[1]     （1为根的情况）
        + dp[1] * dp[0]     （2为根的情况）
  dp[3] = dp[0] * dp[2]      (1为根的情况)
        + dp[1] * dp[1]      (2为根的情况)
        + dp[2] * dp[0]      (3为根的情况) 
  ...
  dp[n+1] = `\sum_{i=0}^n`dp[i]*dp[n-i]    for n>=0
  ```

