## Problem

Given a singly linked list, determine if it is a palindrome.

**Example 1:**

```
Input: 1->2
Output: false
```

**Example 2:**

```
Input: 1->2->2->1
Output: true
```

**Follow up:**
Could you do it in O(n) time and O(1) space?



## Solution

* 使用一个list存储所有元素，然后比较反向list和当前list是否一致
* 使用两个指针，把列表后半部分翻转，在同时从头尾开始移动，如果有值不等就不是，如果都相等就是回文。