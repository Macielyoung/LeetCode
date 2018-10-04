#-*- coding: UTF-8 -*-
import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        length = int(math.ceil(area ** 0.5))
        res = []
        while(1):
            if(area % length == 0):
                res.append(length)
                width = area / length
                res.append(width)
                return res
            length += 1

    def constructRectangle2(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        n = int(area ** 0.5)
        while area % n != 0:
            n -= 1
        return [area // n, n]

if __name__ == '__main__':
    solu = Solution()
    area = 8
    res = solu.constructRectangle2(area)
    print(res)