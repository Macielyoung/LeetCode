## Problem

Given preorder and inorder traversal of a tree, construct the binary tree.

**Note:**
You may assume that duplicates do not exist in the tree.

For example, given

```
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
```

Return the following binary tree:

```
    3
   / \
  9  20
    /  \
   15   7
```

 

## Solution

* 递归。首先根据前序判断数组第一个元素必为root节点，返回中序数组找到root值，将数据分成两半，分别表示左右子树，同时前序数据根据中序左右子树个数同样可以划分为左右子树，借此调用递归。