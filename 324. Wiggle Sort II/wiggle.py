#-*- coding: UTF-8 -*-

class Solution(object):
    # 一些特殊case无法通过，考虑不够周到（如：nums = [5,3,1,2,6,7,8,5,5]）
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        nums.sort()
        half = len(nums) // 2
        nums[:half] = nums[:half][::-1]
        # print(nums)
        i = 1
        j = len(nums) - 1
        while j > len(nums)//2:
            val = nums.pop()
            nums.insert(i, val)
            i += 2
            j -= 1

    # 时间空间复杂度都较高
    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        for i in range(0, len(nums), 2): nums[i] = arr.pop()

    # 后一半和前一半逆序交叉插入
    def wiggleSort3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

if __name__ == '__main__':
    solu = Solution()
    nums = [4,5,5,6]
    solu.wiggleSort3(nums)
    print(nums)