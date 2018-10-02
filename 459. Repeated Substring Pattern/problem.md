## Problem

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

**Example 1:**

```
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
```

**Example 2:**

```
Input: "aba"
Output: False
```

**Example 3:**

```
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
```



## Solution

* 子串长度[1, n/2]，然后乘以对应的倍数，看是否和原字符串相同。
* 看看s是否在2s[1:-1]中。如果它是子串的倍数，那么两倍再去头去尾还是存在这个字符串的。