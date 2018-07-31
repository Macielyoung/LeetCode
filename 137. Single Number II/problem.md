## Problem

Given a **non-empty** array of integers, every element appears *three* times except for one, which appears exactly once. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**

```
Input: [2,2,3,2]
Output: 3
```

**Example 2:**

```
Input: [0,1,0,1,0,1,99]
Output: 99
```



## Solution

* 利用collections包中的Counter方法，统计各个元素出现的次数。
* 使用集合求出所有出现的元素
* 利用真值表(具有扩展性)。