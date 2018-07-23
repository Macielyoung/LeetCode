## Problem

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
```

Return:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

 

## Solution

* 深度优先遍历。使用一个列表一层层向下遍历，当遍历到叶节点时，如果sum等于权重和，则是一条有效路径，加入到结果中；否则不是有效路径，跳过这个结果。

