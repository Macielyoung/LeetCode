## Problem

We are playing the Guess Game. The game is as follows:

I pick a number from **1** to **n**. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay **$x**. You win the game when you guess the number I picked.

**Example:**

```
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
```

Given a particular **n ≥ 1**, find out how much money you need to have to guarantee a **win**.



## Solution

* 刚开始把这个题目想的太简单了，认为最差就是一直选择中位数，每次都选偏大的一侧即可，这样不对的。举个简单的例子，n=4，我先选2，那么剩下的3和4选择加起来至少需要5；而如果先选3，偏小的话只要再选1即可得出结果，这样总共花费$4即可。
* 这题使用动态规划来做。