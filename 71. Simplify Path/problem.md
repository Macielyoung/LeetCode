## Problem

Given an absolute path for a file (Unix-style), simplify it.

For example,
**path** = `"/home/"`, => `"/home"`
**path** = `"/a/./b/../../c/"`, => `"/c"`

**Corner Cases:**

- Did you consider the case where **path** = `"/../"`?
  In this case, you should return `"/"`.
- Another corner case is the path might contain multiple slashes `'/'` together, such as `"/home//foo/"`.
  In this case, you should ignore redundant slashes and return `"/home/foo"`.



## Solution

* 使用split方法将字符串先分割成一个个元素，同时去除空元素。调用一个stack，如果是".."元素，判断stack是否为空，若不是，则去除栈顶元素，若是，则不管，其余元素则要添加进stack中。注意当元素为"."时，跳过。