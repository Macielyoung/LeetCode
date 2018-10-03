#-*- coding: UTF-8 -*-
import random

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand7(self):
        return random.randint(1, 7)

    def rand10(self):
        """
        :rtype: int
        """
        sum = 0
        for i in range(5):
            sum += self.rand7()
        res = sum%10+1
        return res

    def rand102(self):
        """
        :rtype: int
        """
        a = 0
        while a < 2:  # generate an even number with probability 1/2, given a > 1
            a = self.rand7()
        res = 0
        # Roll to determine if the number is going to be 1,2,3,4,5 or 6,7,8,9,10
        if a % 2:
            res += 5
        b = 69
        # generate a number within the chosen range with prob 1/5
        while b > 5:
            b = self.rand7()
        return res + b

if __name__ == '__main__':
    solu = Solution()
    num = solu.rand102()
    print(num)