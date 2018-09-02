#-*- coding: UTF-8 -*-

class Solution(object):
    # 超时
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n==1 or n==2 or n==3):
            return True
        res = (not self.canWinNim(n-1)) or (not self.canWinNim(n-2)) or (not self.canWinNim(n-3))
        return res

    # 看是不是4的倍数
    def canWinNim2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return not n % 4 == 0

if __name__ == '__main__':
    solu = Solution()
    n = 7
    res = solu.canWinNim2(n)
    print(res)
