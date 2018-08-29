## Problem

Given an integer array of size *n*, find all elements that appear more than `⌊ n/3 ⌋` times.

**Note:** The algorithm should run in linear time and in O(1) space.

**Example 1:**

```
Input: [3,2,3]
Output: [3]
```

**Example 2:**

```
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
```



## Solution

* 统计各个数字出现的次数。
* 二赢问题。求列表中所有超过`⌊ n/3 ⌋`长的元素，因此可以知道有三种情况，0个、1个或2个符合条件的数。统计人群中的多数，保留这两位，最后遍历一遍看是否超过1/3长度。

