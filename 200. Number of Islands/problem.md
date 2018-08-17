## Problem

Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

**Example 1:**

```
Input:
11110
11010
11000
00000

Output: 1
```

**Example 2:**

```
Input:
11000
11000
00100
00011

Output: 3
```



## Solution

* 使用BFS，如果当前节点为1，则访问过后将其置为0，并访问其四周的四个节点，一次迭代下去，最终统计沙滩个数。