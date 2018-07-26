## Problem

Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.

**Note:**

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**

```
Input: [2,2,1]
Output: 1
```

**Example 2:**

```
Input: [4,1,2,1,2]
Output: 4
```



## Solution

* 法一，异或技巧。任何两个相同的数异或后结果为1，任何数和0异或后结果为这个数本身。（a^a^b = b）
* 法二，使用集合（collections包）中的Counter类，对数组进行统计，次数为1的即为需要求解的数。