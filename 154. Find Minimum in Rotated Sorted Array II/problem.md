## Problem

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).

Find the minimum element.

The array may contain duplicates.

**Example 1:**

```
Input: [1,3,5]
Output: 1
```

**Example 2:**

```
Input: [2,2,2,0,1]
Output: 0
```



## Solution

* 注意各种corner case，由于数组可以出现重复数字。使用二分检索的时候，当中间的数和右边的数字相等的时候，最右左移一位来看看是不是这段区间是不是都是重复数字。