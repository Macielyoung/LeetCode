## Problem

给定一个整数 *n*，生成所有由 1 ... *n* 为节点所组成的 **二叉搜索树** 。

 

**示例：**

```
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

 

**提示：**

- `0 <= n <= 8`



## Solution

1. 我们从序列[1, n]取出数字i，作为当前的树根，则i-1个数字作为左子树，剩余n-i个元素作为右子树。这样会产生G(i-1)种左子树和G(n-i)种右子树，其中G是卡特兰数。递归使用该方式，可以得到所有的树结构。