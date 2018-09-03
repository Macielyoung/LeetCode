#-*- coding: UTF-8 -*-

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        i = 0
        while i < n:
            if(nums[i]==0):
                nums.pop(i)
                nums.append(0)
                n -= 1
            else:
                i += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastZero = 0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[lastZero], nums[i] = nums[i], nums[lastZero]
                lastZero += 1


if __name__ == '__main__':
    solu = Solution()
    nums = [3, 4, 0, 6, 10, 3, 0, 12, 0, 0, 21, 44, 21, 0, 15]
    solu.moveZeroes2(nums)
    print(nums)