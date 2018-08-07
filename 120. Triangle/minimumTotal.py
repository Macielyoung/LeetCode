#-*- coding: UTF-8 -*-

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        height = len(triangle)
        if height == 1:
            return triangle[0][0]
        for i in range(1, height):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[height-1])

if __name__ == "__main__":
    solu = Solution()
    triangle = [
                     [2],
                    [3,4],
                   [6,5,7],
                  [4,1,8,3]
                ]
    res = solu.minimumTotal(triangle)
    print(res)
