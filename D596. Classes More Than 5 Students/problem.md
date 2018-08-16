## Problem

There is a table `courses` with columns: **student** and **class**

Please list out all classes which have more than or equal to 5 students.

For example, the table:

```
+---------+------------+
| student | class      |
+---------+------------+
| A       | Math       |
| B       | English    |
| C       | Math       |
| D       | Biology    |
| E       | Math       |
| F       | Computer   |
| G       | Math       |
| H       | Math       |
| I       | Math       |
+---------+------------+
```

Should output:

```
+---------+
| class   |
+---------+
| Math    |
+---------+
```



## Solution

查询选修人数大于等于五人的课程。

* 按课程分类，同时使得选修该课的人员>=5。(注意重复人员，使用distinct)

```
select class from courses 
group by class 
having count(distinct student) >= 5
```

