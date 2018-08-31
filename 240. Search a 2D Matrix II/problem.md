## Problem

Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

**Example:**

Consider the following matrix:

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

Given target = `5`, return `true`.

Given target = `20`, return `false`.



## Solution

* 从矩阵右上角元素开始比较，如果target比矩阵元素大，则向下移动；如果target比矩阵元素小，则向左移动，如果相等则说明存在这个矩阵中，直至查找的值到达边界仍没有找到，说明不在矩阵中。