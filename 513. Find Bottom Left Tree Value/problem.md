## Problem

Given a binary tree, find the leftmost value in the last row of the tree.

**Example 1:**

```
Input:

    2
   / \
  1   3

Output:
1
```



**Example 2:** 

```
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
```



**Note:** You may assume the tree (i.e., the given root node) is not **NULL**.



## Solution

* 分层遍历，最后取最下层的第一个元素。
* 记住最后一层插入的节点即可。最左边的是第一个元素。