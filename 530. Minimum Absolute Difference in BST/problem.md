## Problem

Given a binary search tree with non-negative values, find the minimum [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) between values of any two nodes.

**Example:**

```
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
```

 

**Note:** There are at least two nodes in this BST.



## Solution

* 将所有节点值记录下来，排序后求节点之间最小差值。
* 注意是二叉搜索树，所以只要中序遍历就是有序的。