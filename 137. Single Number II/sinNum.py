#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    #使用字典求出所有元素出现的次数
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = Counter(nums)
        for val in dict:
            if dict[val] == 1:
                return val

    #使用集合求出所有出现的元素
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set(nums)
        ele = (sum(elements)*3 - sum(nums)) // 2
        return ele

    #使用真值表（具有推广性）
    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = high = 0
        for val in nums:
            low = (low ^ val) & ~high
            high = (high ^ val) & ~low
        return low

if __name__ == '__main__':
    solu = Solution()
    nums = [0,1,0,1,0,1,99]
    res = solu.singleNumber(nums)
    res2 = solu.singleNumber2(nums)
    res3 = solu.singleNumber3(nums)
    print(res, res2, res3)