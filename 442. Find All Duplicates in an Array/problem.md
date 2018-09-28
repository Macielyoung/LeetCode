## Problem

Given an array of integers, 1 ≤ a[i] ≤ *n* (*n* = size of array), some elements appear **twice** and others appear **once**.

Find all the elements that appear **twice** in this array.

Could you do it without extra space and in O(*n*) runtime?



**Example:**

```
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```



## Solution

* 使用Counter统计词频，需借助额外空间。
* 遍历list中的数字，对数字取负，当再次访问到某个元素是负的时候即是多次出现的元素，加入res中。