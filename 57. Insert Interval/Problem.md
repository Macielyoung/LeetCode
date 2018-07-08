## Problem

Given a set of *non-overlapping* intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

 **Example 1**

```
Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

**Example 2**

```
Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```



## Solution

* 方法一

  首先判断原始intervals是否为空，若是则直接返回newInterval。否则，将newInterval加入到intervals列表中，并使用merge intervals的方法

* 方法二

  使用二分查找法，将所有start和end放入列表中，寻找newInterval的start和end的位置。如果end位置为0，则表示它小于最小的元素，直接返回[newInterval] + intervals；如果start的位置为intervals的长度，则表示它大于最大的元素，直接返回intervals + [newInterval]；否则表示它在元素中间，根据它的位置，构建中间段元素新的区间（比较左右start和end大小），并和左边右边的区间连接起来。