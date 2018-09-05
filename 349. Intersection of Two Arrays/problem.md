## Problem

Given two arrays, write a function to compute their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

**Note:**

- Each element in the result must be unique.
- The result can be in any order.



## Solution

* 求交集。直接使用set交集运算
* 挨个判断num1中元素是否在num2中