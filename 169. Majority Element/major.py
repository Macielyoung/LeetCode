#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = Counter(nums)
        maxVal = dict[nums[0]]
        max = nums[0]
        for val in dict:
            if dict[val] > maxVal:
                max = val
        return max

    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        listnew = sorted(nums)
        num = len(listnew)
        return listnew[num//2]

if __name__ == '__main__':
    solu = Solution()
    nums = [3,2,3]
    res = solu.majorityElement(nums)
    res1 = solu.majorityElement2(nums)
    print(res, res1)