## Problem

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```

But the following `[1,2,2,null,3,null,3]` is not:

```
    1
   / \
  2   2
   \   \
   3    3
```

 

## Solution

* 递归。当左右节点都存在时，比较两个节点node1和node2值是否相等，同时比较node1的左子树是否等于node2的右子树，node1的右子树是否等于node2的左子树。否则比较两个节点。