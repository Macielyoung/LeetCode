## Problem

Invert a binary tree.

**Example:**

Input:

```
     4
   /   \
  2     7
 / \   / \
1   3 6   9
```

Output:

```
     4
   /   \
  7     2
 / \   / \
9   6 3   1
```



## Solution

* 递归法。翻转一个节点的左右孩子，你需要先翻转它的左孩子和右孩子（自下而上考虑）。
* 迭代法。使用一个stack，从上而下分层翻转。