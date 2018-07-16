## Problem

Given an integer *n*, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.

**Example:**

```
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```



## Solution

* 动态规划

1. 选出根结点后分别求该根的左右子树集合，也就是根的左子树有若干种情况，组成左子树集合，右子树也有若干种情况，组成右子树集合
2. 然后将左右子树相互配对，每一个左子树都与所有右子树配对，每一个右子树都与左子树配对，最后将左右子树插入到根结点中。
3. 将根结点放入列表中。