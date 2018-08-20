## Problem

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

**Example 1:**

```
Input: [5,7]
Output: 4
```

**Example 2:**

```
Input: [0,1]
Output: 0
```

 

## Solution

* 比较m和n，看看从高位起有几位数是相同的。
* 从n开始，一直和n-1做与运算，如果值比m大则继续，否则等于n。