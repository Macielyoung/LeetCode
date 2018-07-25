## Problem

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

```
    1
   / \
  2   5
 / \   \
3   4   6
```

The flattened tree should look like:

```
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```



## Solution

* 注意题干中的in-place，即在原地实现。先用一个stack将右子树保存起来，对左子树进行排序，然后在递归到右孩子节点。