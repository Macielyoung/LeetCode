#-*- coding: UTF-8 -*-

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        #动态规划
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        res = [[0]*col for i in range(row)]
        if(obstacleGrid[0][0] == 1):
            return 0
        else:
            res[0][0] = 1

        for i in range(row):
            for j in range(col):
                if(obstacleGrid[i][j]==0):
                    if i>0:
                        res[i][j] += res[i-1][j]
                    if j>0:
                        res[i][j] += res[i][j-1]
        return res[row-1][col-1]

if __name__ == '__main__':
    solu = Solution()
    obstacleGrid = [[0,0,0,1],
                    [0,1,0,0],
                    [0,0,0,0]]
    output = solu.uniquePathsWithObstacles(obstacleGrid)
    print(output)

