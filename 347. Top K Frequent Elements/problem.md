## Problem

Given a non-empty array of integers, return the **k** most frequent elements.

**Example 1:**

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Example 2:**

```
Input: nums = [1], k = 1
Output: [1]
```

**Note:**

- You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
- Your algorithm's time complexity **must be** better than O(*n* log *n*), where *n* is the array's size.



## Solution

* 建立一个最大堆，存放最大的k个数
* 使用Counter对象的原生方法most_common，找出最大值
* 使用bucket sort，建立frequence — num映射，然后从大到小依次加入k个数
* 将key，value作为一对插入到一个list中，然后list根据每个对象的第二个元素来排序（逆序），从中取出k个