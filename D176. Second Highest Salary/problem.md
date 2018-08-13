## Problem

Write a SQL query to get the second highest salary from the `Employee` table.

```
+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
```

For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.

```
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+
```



## Solution

查找第二高工资。

* 除去最高工资后的最高工资：select max(Salary) as SecondHighestSalary from Employee
  where Salary < (select max(Salary) from Employee)

* 使用limit、offset语法：select ( select distinct Salary from Employee
                                           order by Salary desc limit 1,1 ) as SecondHighestSalary

  返回从offset开始的limit条记录。 （效果等同于limit(a,b)）