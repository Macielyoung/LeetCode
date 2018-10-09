## Problem

Given a binary search tree (BST) with duplicates, find all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
- The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
- Both the left and right subtrees must also be binary search trees.

 

For example:
Given BST `[1,null,2,2]`,

```
   1
    \
     2
    /
   2
```

 

return `[2]`.

**Note:** If a tree has more than one mode, you can return them in any order.

**Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).



## Solution

* 逐层扫描所有元素，记录元素出现次数，最终统计出现最频繁的项（没有考虑二叉搜索树的特性）。
* 使用中序遍历二叉搜索树，这样得出的数值按增序输出，同时比较当前的点和前一个点的数值，如果相同，则出现次数加1，统计每个数字的次数，如果当前数字出现次数高于最大次数，则结果中直接变成该数值，如果等于最大次数，则结果中加入该数值。（本题是把中序遍历二叉树和遍历增序数组统计数字频次有机结合起来了）