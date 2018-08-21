## Problem

Remove all elements from a linked list of integers that have value **val**.

**Example:**

```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```



## Solution

* 使用pre和cur两个节点来遍历。使用一个节点记录当前节点的前一个节点，当当前节点值等于删除值，前一个节点的next等于当前节点的next。
* 只用一个节点来遍历。看cur.next的值是否等于val。