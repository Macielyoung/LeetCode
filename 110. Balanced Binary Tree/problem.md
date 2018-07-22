## Problem

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.

**Example 1:**

Given the following tree `[3,9,20,null,null,15,7]`:

```
    3
   / \
  9  20
    /  \
   15   7
```

Return true.
**Example 2:**

Given the following tree `[1,2,2,3,3,null,null,4,4]`:

```
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

Return false.



## Solution

* 使用迭代法，同时回归树的高度和平衡状态。判断一棵树是否平衡需要判断其左右子树是否平衡，同时判断其左右子树高度差知否小于等于1.（明白判断条件即可写出递归函数）。