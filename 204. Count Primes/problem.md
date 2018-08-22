## Problem

Count the number of prime numbers less than a non-negative number, **n**.

**Example:**

```
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```



## Solution

* 一个个判断数是否为质数很明显是超时的。
* 从0开始，如果是质数，那么在n以内它的倍数都不是质数，使用排除法来统计质数个数。