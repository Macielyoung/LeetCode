#-*- coding: UTF-8 -*-

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            n = nums.pop(-1)
            print(n)
            nums.insert(0, n)

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l = len(nums)-k
        nums[:l] = nums[:-k][::-1]
        nums[l:] = nums[l:][::-1]
        nums[:] = nums[::-1]

if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solu.rotate2(nums, k)
    print(nums)