## Problem

Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.

```
+----+-------+
| Id | Score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
```

For example, given the above `Scores` table, your query should generate the following report (order by highest score):

```
+-------+------+
| Score | Rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```

 

## Solution

对用户得分进行排序，同分同名，且不影响下一位用户的排名。

* 计算得分比当前用户得分高的数量。

  select Score, (select count(distinct Score) from Scores where Score >= s.Score) as Rank
  from Scores s
  order by Score desc

* 使用两个表外联，统计一张表中得分大于等于另一张表得分的数量。

  select s.Score, count(distinct t.Score) Rank
  from Scores s Join Scores t on s.Score <= t.Score
  Group By s.Id
  order by s.Score desc