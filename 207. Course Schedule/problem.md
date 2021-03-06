## Problem

There are a total of *n* courses you have to take, labeled from `0` to `n-1`.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`

Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

**Example 1:**

```
Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
```

**Example 2:**

```
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

**Note:**

1. The input prerequisites is a graph represented by **a list of edges**, not adjacency matrices. Read more about [how a graph is represented](https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs).
2. You may assume that there are no duplicate edges in the input prerequisites.



## Solution

* 开始想法是根据关联边，把所有课程构建成一个链表，看看链表是否存在环，如果有，则不能完成。结果发现一个课程可是是多个课程的预学课，所以这个方法是行不通的。
* 判断图中是否有环，使用dfs或bfs遍历，如果每个点存在环，就不能完成课程，如果都没有，则可以完成课程。

```
判断图中是否有环，深度优先遍历：
def dfs(node, graph, visited, stack):
    visited[node] = True
    stack.append(node)
    if node in graph:
        for n in graph[node]:
            if n not in stack:
                if not visited[n]:
                    dfs(n, graph, visited, stack)
            else:
                index = stack.index(n)
                print 'Circle: ',
                for i in stack[index:]:
                    print i,
                print n
    stack.pop(-1)
```

