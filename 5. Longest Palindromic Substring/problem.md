## Problem

Given a string `s`, find the longest palindromic substring in `s`. You may assume that the maximum length of `s` is 1000.

```
Example 1 :

Input : "babad"

Output : "bab"
```

```
Example 2 :

Input : "cbbd"

Output : "bb"
```



## Solution

* 暴力遍历，挨个遍历所有的情况，时间复杂度O(n^3)
* 中心向外扩展。根据回文字符串分单双核，单核是长度为奇数，双核是长度为偶数。遍历字符串中除最后一个位置的字符。单核：low=high，然后向两侧扩散，如果字符不同则终止，同时长度要和目前最长的子串长度比较。双核：high=low+1，其余和单核相同。