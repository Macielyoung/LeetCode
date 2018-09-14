## Problem

Given a *n* x *n* matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

**Example:**

```
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
```



**Note:** 
You may assume k is always valid, 1 ≤ k ≤ n2.



## Solution

* 将matrix转化成list，对它排序取第k小元素。
* 使用最大堆来对元素插入，直到堆满。
* 使用二分查找，每次查找有多少个元素比中值小，以此来调整区间。