## Problem

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```

The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).

**Note:**

Bonus point if you are able to do this using only *O*(*n*) extra space, where *n* is the total number of rows in the triangle.



## Solution

* 动归。考虑每一层的和，其中第一个和最后一个数字只需考虑他们上方的一个数字，而中间的数字则需要考虑上方两侧较小的和，最终返回最后一层最小和。