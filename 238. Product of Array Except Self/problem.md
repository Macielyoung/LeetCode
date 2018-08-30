## Problem

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Example:**

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

**Note:** Please solve it **without division** and in O(*n*).

**Follow up:**
Could you solve it with constant space complexity? (The output array **does not** count as extra space for the purpose of space complexity analysis.)



## Solution

* 直接累乘所有得出总的乘积，再除以每个数。（不能使用除法，所以不行）
* 遍历两次列表，第一次从前往后，第二次从后往前，避开当前位置，即可得出结果。