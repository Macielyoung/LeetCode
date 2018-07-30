#-*- coding: UTF-8 -*-

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1 for i in range(rowIndex+1)]
        for row in range(2, rowIndex+1):
            l2 = 1
            for col in range(1, row):
                l1 = res[col]
                res[col] = res[col] + l2
                l2 = l1
        return res

if __name__ == '__main__':
    solu = Solution()
    row = 4
    res = solu.getRow(row)
    print(res)