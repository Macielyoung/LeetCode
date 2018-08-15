## Problem

Clone an undirected graph. Each node in the graph contains a `label` and a list of its `neighbors`.

 

OJ's undirected graph serialization:

Nodes are labeled uniquely.

 We use `#` as a separator for each node, and `,` as a separator for node label and each neighbor of the node. 

As an example, consider the serialized graph `{0,1,2#1,2#2,2}`.

The graph has a total of three nodes, and therefore contains three parts as separated by `#`.

1. First node is labeled as `0`. Connect node `0` to both nodes `1` and `2`.
2. Second node is labeled as `1`. Connect node `1` to node `2`.
3. Third node is labeled as `2`. Connect node `2` to node `2` (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

```
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
```



## Solution

* 深度遍历（DFS）。使用一个全局访问字典，如果该节点没有访问过，则遍历它，添加到当前节点的neighbors；否则将访问字典中该节点的内容加入到neighbors中。