#-*- coding: UTF-8 -*-

class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix)==0:
            self.data = []
        else:
            m, n = len(matrix), len(matrix[0])
            # 这种初始化方式会导致赋值时整个一列都发生变化，需要注意。这种方式是浅拷贝。
            # self.data = [[0]*n]*m
            self.data = [[0 for i in range(n + 1)] for j in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    self.data[i + 1][j + 1] = self.data[i + 1][j] + self.data[i][j + 1] - self.data[i][j] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if (len(self.data) == 0):
            return 0
        return self.data[row2 + 1][col2 + 1] - self.data[row2 + 1][col1] - self.data[row1][col2 + 1] + self.data[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

if __name__ == '__main__':
    matrix1 = []
    matrix2 = [[3, 0, 1, 4, 2],
              [5, 6, 3, 2, 1],
              [1, 2, 0, 1, 5],
              [4, 1, 0, 1, 7],
              [1, 0, 3, 0, 5]
             ]
    obj = NumMatrix(matrix1)
    print(obj.data)
    res1 = obj.sumRegion(2,1,4,3)
    res2 = obj.sumRegion(1,1,2,2)
    res3 = obj.sumRegion(1,2,2,4)
    print(res1, res2, res3)