## Problem

Given a collection of intervals, merge all overlapping intervals.

 **Example 1**

```
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

**Example 2**

```
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
```



## Solution

* 方法一

  如果intervals为空，则直接返回[]。如果不是空，则先根据列表元素的start元素从小到大排序，然后从第二个元素开始依次和第一个元素比较，如果start元素小于第一个元素的end元素，则合并，考虑end元素之间的大小，同时从intervals中删除第二个元素；否则表示第一个元素不能和其余元素merge，跨到第二个元素开始，以此类推。