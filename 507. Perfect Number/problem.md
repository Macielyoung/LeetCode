## Problem

We define the Perfect Number is a **positive** integer that is equal to the sum of all its **positive** divisors except itself.

Now, given an 

integer

 n, write a function that returns true when it is a perfect number and false when it is not.



**Example:**

```
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
```



**Note:** The input number **n** will not exceed 100,000,000. (1e8)



## Solution

* 直接求所有因子的和，看是否和num相等。(注意特例1，它的因子就是它本身)