#-*- coding: UTF-8 -*-

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        flag = 0
        if num == 0:
            return "0"
        if num < 0:
            num = abs(num)
            flag = 1
        string = ""
        while num:
            string += str(num % 7)
            num = num / 7
        string = string[::-1]
        if flag:
            string = "-"+string
        return string

if __name__ == '__main__':
    solu = Solution()
    num = 0
    res = solu.convertToBase7(num)
    print(res)