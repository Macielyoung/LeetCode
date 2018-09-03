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

if __name__ == '__main__':
    solu = Solution()
    nums = [0,1,0,3,12]
    solu.moveZeroes(nums)
    print(nums)