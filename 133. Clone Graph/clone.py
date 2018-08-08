#-*- coding: UTF-8 -*-

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def dfs(self, node):
        cur = UndirectedGraphNode(node.label)
        self.visited[node] = cur

        for neigh in node.neighbors:
            if neigh not in self.visited:
                cur.neighbors.append(self.dfs(neigh))
            else:
                cur.neighbors.append(self.visited[neigh])
        return cur

    def cloneGraph(self, node):
        self.visited = {}

        if not node:
            return None
        return self.dfs(node)

if __name__ == "__main__":
    solu = Solution()
    A = UndirectedGraphNode(0)
    B = UndirectedGraphNode(1)
    C = UndirectedGraphNode(2)
    A.neighbors = [B, C]
    B.neighbors = [A, C]
    C.neighbors = [A, B, C]
    res = solu.cloneGraph(A)
    print(res.label)
    for i in res.neighbors:
        print(i.label)