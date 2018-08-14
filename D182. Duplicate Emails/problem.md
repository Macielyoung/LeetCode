## Problem

Write a SQL query to find all duplicate emails in a table named `Person`.

```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
```

For example, your query should return the following for the above table:

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+
```



## Solution

查询重复邮箱。

* 判断条件：邮箱相同，Id不同。

  select distinct p1.Email as Email from Person p1, Person p2
  where p1.Email = p2.Email and p1.Id != p2.Id

* 按邮箱分组，如果id数量大于1，即为重复邮箱。

  select Email from Person
  group by Email having count(Id) > 1