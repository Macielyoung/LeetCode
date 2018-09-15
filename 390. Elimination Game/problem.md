## Problem

There is a list of sorted integers from 1 to *n*. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length *n*.

**Example:**

```
Input:
n = 9,
1 2 3 4 5 6 7 8 9
2 4 6 8
2 6
6

Output:
6
```



## Solution

* 按照规则依次删除元素。空间复杂度较高O(n)。
* 使用递归方法。如果n大于1，且是从左往右的话，我们返回2倍的对n/2的从右往左的遍历；如果是从右往左的话，稍稍麻烦一些，我们肯定还是要对n/2调用递归函数的，但是要分奇偶情况，如果n为奇数，返回2倍的对n/2的从左往右的遍历的值；如果n为偶数，2倍的对n/2的从左往右的遍历的值，再减去1。
* 第一次从左往右删除的时候，奇数都被删掉了，剩下的都是偶数。如果我们对所有数都除以2，那么得到一个1到n/2的新数列。下一次我们从右往左删出，那么返回的结果应该是调用递归的结果lastRemaining(n / 2)在数组1到n/2之间的镜像。何为镜像，比如1, 2, 3, 4这个数字，2的镜像就是3, 1的镜像是4。
* 迭代法。我们可以发现从左往右删的时候，每次都是删掉第一个数字，而从右往左删的时候，则有可能删掉第一个或者第二个数字，而且每删一次，数字之间的距离会变为之前的两倍。我们要做的是每次记录当前数组的第一个数字，而且我们再通过观察可以看出，从右往左删时，如果剩下的数字个数是偶数个时，删掉的是第二个数字；如果是奇数个的时候，删掉的是第一个数字。

```
n = 8
1 2 3 4 5 6 7 8
   2  4   6   8
   2      6
          6
          
n = 7      
1 2 3 4 5 6 7
   2  4   6
      4
```