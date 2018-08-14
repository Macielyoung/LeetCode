## Problem

Given a binary tree

```
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
```

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

Initially, all next pointers are set to `NULL`.

**Note:**

- You may only use constant extra space.
- Recursive approach is fine, implicit stack space does not count as extra space for this problem.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

**Example:**

Given the following perfect binary tree,

```
     1
   /  \
  2    3
 / \  / \
4  5  6  7
```

After calling your function, the tree should look like:

```
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL
```



## Solution

* 使用一个dict来分别存储当前层的所有节点，以层级为索引。然后将列表元素的next指针指向下一个元素。
* 使用循环，记录当前节点和前一个节点。如果前一个节点next指针非空，则当前节点的右孩子next指针指向前一个节点next指针的左孩子节点。cur.right.next = cur.next.left