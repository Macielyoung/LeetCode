## Problem

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Example:**

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note**:

1. You must do this **in-place** without making a copy of the array.
2. Minimize the total number of operations.

 

## Solution

* 使用pop和remove来删除和增加0元素。
* 使用一个元素记录当前0元位置，然后将非0元素和它交换位置，遍历整个列表。