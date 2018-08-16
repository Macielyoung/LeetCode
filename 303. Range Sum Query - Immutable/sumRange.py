#-*- coding: UTF-8 -*-

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.dp = [0 for i in range(len(self.array)+1)]
        if len(self.array) >= 1:
            for k in range(len(self.array)):
                self.dp[k+1] = self.array[k] + self.dp[k]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j+1] - self.dp[i]

if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    res1 = obj.sumRange(0, 2)
    res2 = obj.sumRange(2, 5)
    res3 = obj.sumRange(0, 5)
    print(res1, res2, res3)