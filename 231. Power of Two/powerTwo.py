#-*- coding: UTF-8 -*-

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        while(n!=1):
            if(n%2!=0):
                return False
            else:
                n >>= 1
        return True

if __name__ == '__main__':
    solu = Solution()
    n = 28
    res = solu.isPowerOfTwo(n)
    print(res)