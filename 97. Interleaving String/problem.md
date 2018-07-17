## Problem

Given *s1*, *s2*, *s3*, find whether *s3* is formed by the interleaving of *s1* and *s2*.

**Example 1:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
```

**Example 2:**

```
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
```



## Solution

* 动态规划

  + 首先判断s1和s2长度之和是否等于s3的长度，若不等，则返回False；

  + 接着推倒动态规划的递推公式。当s1和s2为空串时，s3必然为空串，所以边界情况`dp[0][0]`赋值为True；

  + 如果s1和s2其中一个为空串的话，那么另一个肯定和s3的长度相等，然后按位比较。若相同且上一个位置为True则为True，其余都为False，因此我们可以更新得到所有的`dp[0][i]`和`dp[j][0]`；

  + 对于非边缘位置，它的左边或者上边有可能为True或False，两边都可跟新，若一条路跟新为True，则为True。如果左边为True，比较s2和s3对应位置是否相等（s2[j-1] = s3[j-1+i]），若相等则为True，否则为False，上边情况亦如是。最终可得到递推公式：

    `dp[i][j]` =  (`dp[i-1][j]` and s1[i-1]==s3[i-1+j]) or (`dp[i][j-1]` and s2[j-1]==s3[j-1+i])。