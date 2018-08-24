## Problem

Given two strings *s* and *t* , write a function to determine if *t* is an anagram of *s*.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

**Example 2:**

```
Input: s = "rat", t = "car"
Output: false
```

**Note:**
You may assume the string contains only lowercase alphabets.



## Solution

* 使用Counter统计各种字符出现次数，如果两个string各字符一样，则为True，否则为False。
* 对string排序后两者相同也可。