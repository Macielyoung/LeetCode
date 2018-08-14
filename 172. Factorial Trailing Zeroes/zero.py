#-*- coding: UTF-8 -*-

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n > 0):
            n //= 5
            count += n
        return count

if __name__ == '__main__':
    solu = Solution()
    n = 25
    res = solu.trailingZeroes(n)
    print(res)