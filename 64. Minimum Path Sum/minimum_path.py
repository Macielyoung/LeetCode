#-*- coding: UTF-8 -*-

class Solution:
    # 未剪枝，时间复杂度高
    # def minPathSum(self, grid):
    #     """
    #     :type grid: List[List[int]]
    #     :rtype: int
    #     """
    #     if(not grid):
    #         return 0
    #     m = len(grid)-1
    #     n = len(grid[0])-1
    #     length = 0
    #     res = []
    #     self.calPath(0, 0, m, n, grid, length, res)
    #     return min(res)
    #
    # def calPath(self, i, j, m, n, grid, length, res):
    #     if(i==m and j==n):
    #         length += grid[i][j]
    #         res.append(length)
    #         return
    #     if(i<m and j<n):
    #         length += grid[i][j]
    #         self.calPath(i + 1, j, m, n, grid, length, res)
    #         self.calPath(i, j + 1, m, n, grid, length, res)
    #     if(i==m and j<n):
    #         length += grid[i][j]
    #         self.calPath(i, j+1, m, n, grid, length, res)
    #     if(i<m and j==n):
    #         length += grid[i][j]
    #         self.calPath(i+1, j, m, n, grid, length, res)

    # Space : O(m*n)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if(not grid):
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

    # Space : O(2*n)
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        pre = cur = [0] * n
        pre[0] = grid[0][0]
        for i in range(1, n):
            pre[i] = pre[i-1] + grid[0][i]
        for i in range(1, m):
            cur[0] = pre[0] + grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], pre[j]) + grid[i][j]
            pre = cur
        return cur[-1]

    # Space : O(n)
    def minPathSum3(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        cur = [0] * n
        cur[0] = grid[0][0]
        for i in range(1, n):
            cur[i] = cur[i-1] + grid[0][i]
        for i in range(1, m):
            cur[0] += grid[i][0]
            for j in range(1, n):
                cur[j] = min(cur[j-1], cur[j]) + grid[i][j]
        return cur[-1]

    # Space : change the grid itself
    def minPathSum4(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]

if __name__ == '__main__':
    solu = Solution()
    grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    path = solu.minPathSum(grid)
    path2 = solu.minPathSum2(grid)
    path3 = solu.minPathSum3(grid)
    path4 = solu.minPathSum4(grid)
    print(path, path2, path3, path4)