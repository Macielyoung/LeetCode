## Problem

Given an array of integers and an integer *k*, find out whether there are two distinct indices *i* and *j* in the array such that **nums[i] = nums[j]** and the **absolute** difference between *i* and *j* is at most *k*.

**Example 1:**

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

**Example 2:**

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

**Example 3:**

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```



## Solution

* 继续使用217题的比较长度，会超时
* 使用一个dict来存储出现的数字，value存储它的位置，如果出现同样的数字，查看它的位置和value之间的差，如果小于等于k，则存在，否则更新value的值，继续遍历数组。
* 也可以使用一个队列来存放值，最多保存k个值，如果一个新值在queue中，则存在，否则更新queue。