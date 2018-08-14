#-*- coding: UTF-8 -*-

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while(n > 0):
            r = (n-1) % 26
            s += chr(r+65)
            n = (n-1) // 26
        return s[::-1]

if __name__ == '__main__':
    solu = Solution()
    n = 52
    res = solu.convertToTitle(n)
    print(res)