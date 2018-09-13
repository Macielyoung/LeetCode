#-*- coding: UTF-8 -*-

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def __init__(self):
        self.pick = 5

    def guess(self, num):
        if(num > self.pick):
            return -1
        elif(num < self.pick):
            return 1
        else:
            return 0

    # binary search
    # Time:O(logn),  Space:O(1)
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while(low <= high):
            mid = (low + high) / 2
            res = self.guess(mid)
            if(res == 0):
                return mid
            elif(res < 0):
                high = mid - 1
            else:
                low = mid + 1
        return -1

    # Ternary Search
    # Time:O(log_3^n)  Space:O(1)
    def guessNumber2(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while (low <= high):
            three1 = low + (high-low)/3
            three2 = high - (high-low)/3
            res1, res2 = self.guess(three1), self.guess(three2)
            if(res1==0):
                return three1
            if(res2==0):
                return three2
            if(res2 == 1):
                low = three2 + 1
            elif(res1 == -1):
                high = three1 - 1
            else:
                low = three1 + 1
                high = three2 - 1
        return -1

if __name__ == '__main__':
    solu = Solution()
    n = 20
    res = solu.guessNumber2(n)
    print(res)