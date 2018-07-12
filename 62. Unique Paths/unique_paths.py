#-*- coding: UTF-8 -*-
import math

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # down = n - 1
        # all = m + n - 2
        # numerator = denominator = 1
        # for i in range(all, all-down, -1):
        #     numerator *= i
        # for i in range(1,down+1):
        #     denominator *= i
        # res = numerator // denominator
        # return res

        #使用阶乘函数
        return int(math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1)))

if __name__ == '__main__':
    solu = Solution()
    res = solu.uniquePaths(7, 3)
    print(res)