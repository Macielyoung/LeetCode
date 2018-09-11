#-*- coding: UTF-8 -*-

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 0
        if n % 2 == 0:
            return self.integerReplacement(n/2)+1
        else:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1))+1

if __name__ == '__main__':
    solu = Solution()
    n = 30
    res = solu.integerReplacement(n)
    print(res)

