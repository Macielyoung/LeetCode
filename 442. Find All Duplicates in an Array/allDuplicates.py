#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    # Without extra space
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for val in nums:
            if nums[abs(val)-1]<0:
                res.append(abs(val))
            else:
                nums[abs(val)-1] *= -1
        return res

    # Need extra space
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [k for k,v in Counter(nums).items() if v>1]
        return res

if __name__ == '__main__':
    solu = Solution()
    nums = [4,3,2,7,8,2,3,1]
    res = solu.findDuplicates(nums)
    print(res)