#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    # 记录词频
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = Counter(nums)
        for key, value in dict.items():
            if value > 1:
                return key

    # 规约成环问题，时间复杂度O(n)，空间复杂度O(1)
    def findDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

if __name__ == '__main__':
    solu = Solution()
    nums = [1,4,6,6,6,2,3]
    nums2 = [3,1,3,4,2]
    nums3 = [2,5,9,6,9,3,8,9,7,1]
    res = solu.findDuplicate2(nums3)
    print(res)