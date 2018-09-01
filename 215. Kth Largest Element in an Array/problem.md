## Problem

Find the **k**th largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

**Example 1:**

```
Input: [3,2,1,5,6,4] and k = 2
Output: 5
```

**Example 2:**

```
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
```

**Note:** 
You may assume k is always valid, 1 ≤ k ≤ array's length.



## Solution

* 直接排序（逆序），选择第k-1个元素。
* 使用最小堆存储数组（数组存储的都是元素的负数），弹出k个元素。(Python：heapq.heapify创建一个最小堆)
* 利用快排的partition思想，选定一个数组内的值作为pivot，将小于pivot的数字放在左边，大于等于的放右边。接着判断两边数字的数量，如果右边的数量大于k，说明第k大在pivot及左边区域，对左半执行partition函数；如果右边大于k个，说明在pivot及右边区域，对右半执行partition函数。直到右半刚好有k-1个数。
* 使用O(1)的空间复杂度，且不能改变原数组。主要使用两个变量来存储数组最大和最小值，二分法比较数组，统计>=中间数的数量count1和>中间数的数量count2，如果count1>=k且count2<k，则中间数必是第k大的数；如果count1<k，说明比中间大的数太少了，则上界换成中间数-1，继续二分；如果count1>k，说明比中间数大的数太多了，则下届换成中间数+1，继续二分，直至求出解。（这个方法适用整型数）   O(n)时间复杂度。