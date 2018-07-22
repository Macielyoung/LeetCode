## Problem

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,

```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```

return true, as there exist a root-to-leaf path `5->4->11->2` which sum is 22.



## Solution

* 递归法。当该节点为空时返回False。当该节点为叶节点，同时值等于sum则返回True，不等则返回False。
* 使用堆栈，宽度优先遍历，每层中的到叶节点的和如果为sum，则返回True。