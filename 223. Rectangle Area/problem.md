## Problem

Find the total area covered by two **rectilinear** rectangles in a **2D** plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![Rectangle Area](https://leetcode.com/static/images/problemset/rectangle_area.png)

**Example:**

```
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
```

**Note:**

Assume that the total area is never beyond the maximum possible value of **int**.



## Solution

* 映射到坐标轴上来比较横纵坐标是否有交点，如果有求出交集面积，再用两个矩形面积和减去交集面积；如果没有则直接是两个矩形面积和。