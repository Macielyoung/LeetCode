#-*- coding: UTF-8 -*-

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        nsqrt = int((2*n)**0.5)
        sum = nsqrt*(nsqrt-1)
        while(sum<=2*n):
            nsqrt += 1
            sum = nsqrt*(nsqrt-1)
        return nsqrt-2

    def arrangeCoins2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # int is simply to floor the floating point so we get the largest integer smaller than the expression
        return int((math.sqrt(8 * n + 1) - 1) / 2)

if __name__ == '__main__':
    solu = Solution()
    n = 6
    res = solu.arrangeCoins(n)
    print(res)