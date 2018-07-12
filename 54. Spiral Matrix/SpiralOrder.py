#-*- coding: UTF-8 -*-

class Solution:
    def __init__(self):
        self.result = []

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if(len(matrix) == 0):
            return self.result
        self.filter(matrix, 0, 0, len(matrix), len(matrix[0]))
        return self.result

    def filter(self, matrix, x, y, m, n):
        if m <= 0 or n <= 0:
            return
        if m == 1:
            for i in range(n):
                self.result.append(matrix[x][y + i])
            return
        if n == 1:
            for i in range(m):
                self.result.append(matrix[x + i][y])
            return

        # up
        for i in range(n):
            self.result.append(matrix[x][y + i])
        # right
        for i in range(1, m):
            self.result.append(matrix[x + i][y + n - 1])
        # down
        for i in range(n - 2, -1, -1):
            self.result.append(matrix[x + m - 1][y + i])
        # left
        for i in range(m - 2, 0, -1):
            self.result.append(matrix[x + i][y])

        self.filter(matrix, x+1, y+1, m-2, n-2)

if __name__ == '__main__':
    solu = Solution()
    matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
    result = solu.spiralOrder(matrix)
    print(result)