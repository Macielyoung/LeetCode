## Problem

Given a **non-empty** array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

**Example 1:**

```
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
```

**Example 2:**

```
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
```



## Solution

* 给定一个非负整数，使用列表表示，求出加1后的结果。
* 从低位向高位依次传递，遇9向前进位，否则直接当前位加1返回结果。（注意如果最高位也要进位，则添加一位数）