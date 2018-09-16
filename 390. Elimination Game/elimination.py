#-*- coding: UTF-8 -*-
import math

class Solution(object):
    # 内存溢出，空间复杂度高了
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        nums = range(1, n+1)
        flag = 1
        while(len(nums)>1):
            if(flag == 1):
                nums = nums[1::2]
            else:
                nums = nums[-2::-2][::-1]
            flag *= -1
        return nums[0]

        # 精简步骤，直接每次都翻转一下list即可，不需要判断是正序还是逆序
        # if n==1:
        #     return 1
        # nums = range(1, n + 1)
        # while(len(nums)>1):
        #     nums = nums[1::2][::-1]
        # return nums[0]

    def lastRemaining2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 3 or n == 2:
            return 2
        elif n == 1:
            return 1
        else:
            base = 4 * self.lastRemaining2(n / 4)
            if n % 4 == 0 or n % 4 == 1:
                return base - 2
            else:
                return base

    # 递归
    def lastRemaining3(self, n):
        """
        :type n: int
        :rtype: int
        """
        def help(n, order):
            if n==1: return 1
            if order:
                return 2 * help(n/2, False)
            else:
                return 2 * help(n/2, True) - 1 + n % 2
        return help(n, True)

    def lastRemaining4(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 1 if n == 1 else 2 * (1 + n / 2 - self.lastRemaining4(n / 2))

    # 迭代
    def lastRemaining5(self, n):
        """
        :type n: int
        :rtype: int
        """
        base, res = 1, 1
        while (base * 2 <= n):
            res += base
            base *= 2
            if (base * 2 > n):
                break
            if ((n / base) % 2 == 1):
                res += base
            base *= 2
        return res

if __name__ == '__main__':
    solu = Solution()
    n = 13
    res = solu.lastRemaining5(n)
    print(res)