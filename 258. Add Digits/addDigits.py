#-*- coding: UTF-8 -*-

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            string = str(num)
            num = 0
            for i in range(len(string)):
                num += int(string[i])
        return num

    # 除9有余
    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num == 0):
            return 0
        elif(num % 9 ==0):
            return 9
        else:
            return num % 9

if __name__ == '__main__':
    solu = Solution()
    num = 38
    res = solu.addDigits(num)
    print(res)