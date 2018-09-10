## Problem

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

**Example 1:**

```
Input: 16
Output: true
```

**Example 2:**

```
Input: 5
Output: false
```

**Follow up**: Could you solve it without loops/recursion?



## Solution

* 常规解法就是使用迭代法一直除4，看是否可以除尽。
* 根据迭代法可以改成递归法。
* 使用最大的4的次方数，查看num是否是它的因子，同时num除3余1。
* 将4的次方数表示成二进制，可以发现都是首位为1，后面有偶数个0位。