## Problem

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?



## Solution

* 使用两个指针--快慢指针，快指针每次走两步，慢指针走一步，如果他们能重合就存在环，否则不存在。