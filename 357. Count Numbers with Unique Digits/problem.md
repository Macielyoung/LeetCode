## Problem

Given a **non-negative** integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

**Example:**

```
Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
```



## Solution

* 统计所有含有独特数字的数量。

  ```
  使用递推关系：f(n) = f(n-1) + 9*A_{9}^{n-1}
  ```

* 动态规划。