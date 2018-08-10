#-*- coding: UTF-8 -*-

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cursor = nums[0]
        num = len(nums)
        imax = imin = cursor
        for i in range(1, num):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])
            cursor = max(cursor, imax)
        return cursor

if __name__ == '__main__':
    solu = Solution()
    nums = [2,3,-2,4]
    res = solu.maxProduct(nums)
    print(res)
