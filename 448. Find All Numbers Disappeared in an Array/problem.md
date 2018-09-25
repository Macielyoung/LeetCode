## Problem

Given an array of integers where 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear twice and others appear once.

Find all the elements of [1, *n*] inclusive that do not appear in this array.

Could you do it without extra space and in O(*n*) runtime? You may assume the returned list does not count as extra space.

**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
```



## Solution

* 使用Counter统计所有key，再利用set求差集得出未出现的数字。
* 如果一个数字没有出现，那么这个索引对应的数字不能被访问到。所以我们根据每个数字索引的访问，将原来的数字变为负数，最后正数的索引即为没有出现的数字。