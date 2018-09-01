#-*- coding: UTF-8 -*-

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum1 = n*(n+1)//2
        sum2 = sum(nums)
        return sum1-sum2

if __name__ == '__main__':
    solu = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    res = solu.missingNumber(nums)
    print(res)