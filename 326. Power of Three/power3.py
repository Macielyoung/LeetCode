#-*- coding: UTF-8 -*-
import sys
import math

class Solution:
    # 使用循环
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        while(n>1):
            if(n % 3 == 0):
                n //= 3
            else:
                return False
        if(n==1):
            return True

    # 不使用循环，算法思想使用3的最大次方数来整除，因为如果是3的次方数，那么一定是最大次方的因子。
    def isPowerOfThree2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        max3power = 3 ** int(math.log(sys.maxsize, 3))
        return n > 0 and max3power % n == 0


if __name__ == '__main__':
    solu = Solution()
    n1 = 27
    n2 = 5
    n3 = 243
    n4 = 45
    res1 = solu.isPowerOfThree2(n1)
    res2 = solu.isPowerOfThree2(n2)
    res3 = solu.isPowerOfThree(n3)
    res4 = solu.isPowerOfThree(n4)
    print(res1, res2, res3, res4)
