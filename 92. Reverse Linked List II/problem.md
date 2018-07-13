## Problem

Reverse a linked list from position *m* to *n*. Do it in one-pass.

**Note:** 1 ≤ *m* ≤ *n* ≤ length of list.

**Example:**

```
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
```



## Solution

* 移动到需要翻转链表部分的头结点位置，依次翻转节点，至结束位置，再连接上开始和结尾保持不变的部分，注意一些corner case (比如链表为空或者只有一个节点；m和n相同；m等于1即从头结点开始翻转)。