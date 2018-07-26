#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for val in nums:
            res ^= val
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        for val in cnt:
            if cnt[val] == 1:
                return val

if __name__ == '__main__':
    solu = Solution()
    nums = [2, 2, 1]
    nums2 = [4, 1, 2, 1, 2]
    res1 = solu.singleNumber(nums)
    res2 = solu.singleNumber(nums2)
    res3 = solu.singleNumber2(nums)
    print res1, res2, res3
