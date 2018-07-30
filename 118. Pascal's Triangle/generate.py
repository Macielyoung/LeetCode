#-*- coding: UTF-8 -*-

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        res = [[1], [1,1]]
        for i in range(2, numRows):
            row = []
            row.append(1)
            for j in range(1, i):
                val = res[i-1][j-1] + res[i-1][j]
                row.append(val)
            row.append(1)
            res.append(row)
        return res

if __name__ == '__main__':
    solu = Solution()
    rows = 6
    res = solu.generate(rows)
    print(res)