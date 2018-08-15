#-*- coding: UTF-8 -*-

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
        return count

if __name__ == '__main__':
    solu = Solution()
    n = 15
    res = solu.hammingWeight(n)
    print(res)