## Problem

There are *n* bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the *i*-th round, you toggle every *i* bulb. For the *n*-th round, you only toggle the last bulb. Find how many bulbs are on after *n* rounds.

**Example:**

```
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
```



## Solution

* 只有因子个数是奇数个的灯泡操作结束后还是亮着的，所以就是统计[1, n]之间因子个数为奇数的数量。而因子数量为奇数的数只有完全平方数。
* 根据逻辑依次来调整灯泡亮暗。使用1-x来变化状态。