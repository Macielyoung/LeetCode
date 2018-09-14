## Problem

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

**Examples:**

```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```



**Note:** You may assume the string contain only lowercase letters.



## Solution

* 字符串从头开始挨个比较，时间复杂度O(n)。
* 使用Counter来统计出现一次的元素，再取index最小的元素，如果没有就返回-1.