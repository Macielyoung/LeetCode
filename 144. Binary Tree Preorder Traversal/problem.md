## Problem

Given a binary tree, return the *preorder* traversal of its nodes' values.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?



## Solution

* 递归实现。
* 迭代实现。应用一个stack保存当前节点，以便后面查询他的左右节点。