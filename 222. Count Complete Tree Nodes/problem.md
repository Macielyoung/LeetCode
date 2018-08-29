## Problem

Given a **complete** binary tree, count the number of nodes.

**Note:**

**Definition of a complete binary tree from Wikipedia:**
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

**Example:**

```
Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6
```



## Solution

* 因为最后一层节点都是尽可能排在左侧，所以我们尽可能折半统计。统计子树到最右叶节点的高度。如果左子树和右子树高相同，说明最后一层的叶节点不超过左子树，右子树最后一层都没有节点，可以直接使用公式添加个数，并将根结点移动到左孩子节点；如果左子树的高度比右子树大，说明最后一层的叶节点超过左子树，左子树最后一层都有叶节点，可以使用公式添加左子树的个数，并将跟节点移动到右孩子节点。