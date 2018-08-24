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