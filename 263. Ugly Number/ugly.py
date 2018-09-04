#-*- coding: UTF-8 -*-

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num<=0):
            return False
        while(num>1):
            if(num % 2 == 0):
                num //= 2
            else:
                break
        while(num>1):
            if (num % 3 == 0):
                num //= 3
            else:
                break
        while(num>1):
            if (num % 5 == 0):
                num //= 5
            else:
                break
        return num==1

if __name__ == '__main__':
    solu = Solution()
    num = 19
    res = solu.isUgly(num)
    print(res)