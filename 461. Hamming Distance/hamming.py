#-*- coding: UTF-8 -*-

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        res = bin(xor)[2:].count('1')
        return res

if __name__ == '__main__':
    solu = Solution()
    x, y = 1, 4
    res = solu.hammingDistance(x, y)
    print(res)