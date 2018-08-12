## Problem

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- getMin() -- Retrieve the minimum element in the stack.

**Example:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```



## Solution

* 使用另一个list（min）来保存最小值。

  当添加数据时，如果最小值list为空，则直接加入，否则和list最后一个元素比较，当更小的话加入x，否则把最后元素再加入一次到list中。

  弹出元素时，data和min列表都弹出最后一个元素，保持数据量相等。