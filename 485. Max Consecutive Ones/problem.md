## Problem

Given a binary array, find the maximum number of consecutive 1s in this array.

**Example 1:**

```
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
```



**Note:**

- The input array will only contain `0` and `1`.
- The length of input array is a positive integer and will not exceed 10,000



## Solution

* 求出所有0的位置，然后得出后一个值和前一个值的差，取最大值。（注意需要加上开始和结尾两个点：-1和len(nums)）。
* 使用动态规划思想，如果前一个值为1，则加上它，否则当前值置0。
* 转化为string，使用‘0’来分割字符串，取最大子串长度。