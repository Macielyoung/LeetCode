## Problem

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.



## Explanation

python中的对象之间赋值时是按照引用传递的。

* deep copy（深拷贝）。拷贝对象及其子对象。深拷贝是指源对象和拷贝对象相互独立。
* copy（浅拷贝）。只拷贝父对象，不会拷贝对象内部的子对象。浅拷贝是指源对象与拷贝对象共用一份实体，仅仅是引用的变量不同。



## Solution

分三步：

* 首先，在当前链表中每个节点后面拷贝一个同样的节点，并把当前节点的next指向该节点，这个节点的next指向原来的next（复制每个节点的next指针）；
* 其次，把当前节点的随机指针指向节点的后一个节点赋给当前节点后一个节点的随机指针（复制节点的random指针）；
* 最后，把复制的节点从原链表中剥离开。

![copyRandom](https://github.com/Macielyoung/LeetCode/blob/master/138.%20Copy%20List%20with%20Random%20Pointer/copyRandom.jpg)
