## Problem

Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.

**Note:** 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

**Example 1:**

```
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

**Example 2:**

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

**Follow up:**
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



## Solution

* 由于是一颗二叉搜索树，所以一个节点的左孩子总是小于它，右孩子总是大于它，现在求第k小的值，那么我们可以统计一个节点左孩子的数量，如果k小于等于left，说明这个值落在左孩子中；如果k等于left+1，则说明该节点的值就是第k小；否则就是落在右孩子中，递归下去。
* 可以使用中序遍历算法，把所有的值都读取出来，然后取下标为k-1的元素。