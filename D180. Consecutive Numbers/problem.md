## Problem

Write a SQL query to find all numbers that appear at least three times consecutively.

```
+----+-----+
| Id | Num |
+----+-----+
| 1  |  1  |
| 2  |  1  |
| 3  |  1  |
| 4  |  2  |
| 5  |  1  |
| 6  |  2  |
| 7  |  2  |
+----+-----+
```

For example, given the above `Logs` table, `1` is the only number that appears consecutively for at least three times.

```
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
```



## Solution

找连续出现三次以上（包括三次）的数字。

* id相连，num相等。

  select distinct l1.num as ConsecutiveNums from Logs l1, Logs l2, Logs l3
  where l1.id = l2.id - 1 and l2.id = l3.id - 1 and l1.num = l2.num and l2.num = l3.num