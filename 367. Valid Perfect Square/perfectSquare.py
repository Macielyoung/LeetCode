#-*- coding: UTF-8 -*-
import math

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        if float(int(math.sqrt(num))) == math.sqrt(num):
            return True
        else:
            return False

if __name__ == '__main__':
    solu = Solution()
    num = 14
    res = solu.isPerfectSquare(num)
    print(res)