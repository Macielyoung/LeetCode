## Problem

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.

**Example:**

```
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
```

 

## Solution

* 递归法。每次寻找列表中间点作为树的根节点，然后将列表分成两段，前段的中点作为左孩子，后段的中点作为右孩子，依次递归下去。（可以使用一些递归技巧一次性找到列表的中间节点的前一个节点）

  ```
  slow, fast = head, head.next.next
  while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
  ```

  