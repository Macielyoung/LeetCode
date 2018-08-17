#-*- coding: UTF-8 -*-

class Solution(object):
    def __init__(self):
        self.directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def bfs(self, grid, x0, y0):
        grid[x0][y0] = '0'
        for dx, dy in self.directions:
            x = x0 + dx
            y = y0 + dy
            if (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] == '1'):
                self.bfs(grid, x, y)

    def numIslands(self, grid):
        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    counter += 1
        return counter

if __name__ == '__main__':
    solu = Solution()
    grid = [["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"],
            ["0", "0", "0", "1", "0"]]
    res = solu.numIslands(grid)
    print(res)