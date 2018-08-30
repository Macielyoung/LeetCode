#-*- coding: UTF-8 -*-

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        dp = [[0 if matrix[i][j] == '0' else 1 for j in range(m)] for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                if(matrix[i][j]=='1'):
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                else:
                    dp[i][j] = 0
        res = max(max(row) for row in dp)
        return res**2

if __name__ == '__main__':
    solu = Solution()
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    res = solu.maximalSquare(matrix)
    print(res)