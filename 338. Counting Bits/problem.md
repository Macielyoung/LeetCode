## Problem

Given a non negative integer number **num**. For every numbers **i** in the range **0 ≤ i ≤ num** calculate the number of 1's in their binary representation and return them as an array.

**Example 1:**

```
Input: 2
Output: [0,1,1]
```

**Example 2:**

```
Input: 5
Output: [0,1,1,2,1,2]
```

**Follow up:**

- It is very easy to come up with a solution with run time **O(n\*sizeof(integer))**. But can you do it in linear time **O(n)** /possibly in a single pass?
- Space complexity should be **O(n)**.
- Can you do it like a boss? Do it without using any builtin function like **__builtin_popcount** in c++ or in any other language.



## Solution

* 遍历每一个数，统计数的二进制中1的个数

* 通过一个生成方式，数组中每2^n个数生成是前一半的数据值加1的结果

  ```
  [0] ==> start .i.e 0 has 0 1's in it
  [0,1] ==> [0] + 1 + [0] = [0] + [1] = [0,1]
  [0,1,1,2] ==> [0,1] + 1 + [0,1] = [0,1] + [1,2] = [0,1,1,2]
  [0,1,1,2,1,2,2,3] ==> [0,1,1,2] + 1 + [0,1,1,2] = [0,1,1,2] + [1,2,2,3] = [0,1,1,2,1,2,2,3]
  ```

