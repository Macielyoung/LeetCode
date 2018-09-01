## Problem

Given a binary tree, return all root-to-leaf paths.

**Note:** A leaf is a node with no children.

**Example:**

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```



## Solution

* 深度优先遍历。如果是叶节点，则加入该节点，插入到paths中；否则左右孩子分别调用dfs。