## Problem

Reverse bits of a given 32 bits unsigned integer.

**Example:**

```
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
```

**Follow up**:
If this function is called many times, how would you optimize it?



## Solution

* 使用与操作运算，把原始十进制转化为二进制，再转化成string，使用int转变回十进制。
* 使用左移和右移运算。

