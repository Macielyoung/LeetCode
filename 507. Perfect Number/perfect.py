#-*- coding: UTF-8 -*-

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sum = 1
        for i in range(2, int(num**0.5+1)):
            if num%i==0:
                sum += i
                sum += num/i
        return True if sum==num else False

if __name__ == '__main__':
    solu = Solution()
    num = -5
    res = solu.checkPerfectNumber(num)
    print(res)