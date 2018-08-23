#-*- coding: UTF-8 -*-

class Solution:
    # 如果这个点被访问过且置为-1，说明这个点上存在环；
    # 如果这个点被访问过且置为1，说明这个点上不存在环；
    # 如果这个点还没有被访问，置为0
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)]
        visit = [0 for i in range(numCourses)]
        for p, q in prerequisites:
            graph[p].append(q)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':
    solu = Solution()
    numCourses = 3
    prerequisites = [[0,2],[1,2],[2,0]]
    res = solu.canFinish(numCourses, prerequisites)
    print(res)