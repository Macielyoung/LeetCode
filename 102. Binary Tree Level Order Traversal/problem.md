## Problem

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```

return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```



## Solution

* 使用一个列表记录当前层次节点，当把所有节点值加入到返回列表中后，考虑下一层加入到节点，同时删除本层节点（注意：python删除列表元素有remove，pop和del三种方法，谨慎使用，注意它们三者的使用方法及**删除的元素位置**）。