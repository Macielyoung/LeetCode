## Problem

Write a SQL query to get the *n*th highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the *n*th highest salary where *n* = 2 is `200`. If there is no *n*th highest salary, then the query should return `null`.

```
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```



## Solution

查找第N高工资，和上一题第二高一个思路，注意SQL写函数的语法。

* CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
  BEGIN
  Declare M INT;
  SET M = N - 1;
    RETURN (
        # Write your MySQL query statement below.
        select (select distinct Salary from Employee order by Salary desc limit M, 1) as getNthHighestSalary
    );
  END

