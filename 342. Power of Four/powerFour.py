#-*- coding: UTF-8 -*-
import sys
import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        maxPowerFour = 4 ** int(math.log(sys.maxsize, 4))
        return maxPowerFour % num == 0 and num > 0 and num % 3 == 1

    # 递归
    def isPowerOfFour2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True
        return not (num % 4) & self.isPowerOfFour(num // 4)

    # 使用二进制表示转化
    def isPowerOfFour3(self, num):
        """
        :type num: int
        :rtype: bool
        """
        bin_num = bin(num)[2:]
        return bin_num[0] == '1' and bin_num.count('0') == len(bin_num)-1 and bin_num.count('0') % 2 == 0

    # 迭代
    def isPowerOfFour4(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        elif num == 0:
            return False

        while (num != 1):
            if (num % 4 != 0):
                return False
            else:
                num = num / 4
        return True

if __name__ == '__main__':
    solu = Solution()
    num1 = 16
    num2 = 63
    res = solu.isPowerOfFour(num1)
    print(res)