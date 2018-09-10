## Problem

Given an unsorted array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]...`.

**Example 1:**

```
Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
```

**Example 2:**

```
Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
```

**Note:**
You may assume all input has valid answer.

**Follow Up:**
Can you do it in O(n) time and/or in-place with O(1) extra space?



## Solution

* 将数组排序，然后将数组前一半和后一半逆序交叉插入到数组中，即可形成Wiggle Sort。

  ```
  Example nums = [1,2,...,7]      Example nums = [1,2,...,8] 
  
  Small half:  4 . 3 . 2 . 1      Small half:  4 . 3 . 2 . 1 .
  Large half:  . 7 . 6 . 5 .      Large half:  . 8 . 7 . 6 . 5
  --------------------------      --------------------------
  Together:    4 7 3 6 2 5 1      Together:    4 8 3 7 2 6 1 5
  ```