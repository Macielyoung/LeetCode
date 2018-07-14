## Problem

Given a binary tree, return the *inorder* traversal of its nodes' values.

**Example:**

```
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

**Follow up:** Recursive solution is trivial, could you do it iteratively?



## Solution

* 方法一

  中序遍历，使用递归方法，按照左中右的顺序

* 方法二

  非递归，使用一个stack来保存二叉树中的节点，左节点优先。

  