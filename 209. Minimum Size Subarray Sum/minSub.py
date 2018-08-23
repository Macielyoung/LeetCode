#-*- coding: UTF-8 -*-

class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = left = 0
        result = len(nums)+1
        for right, n in enumerate(nums):
            total += n
            while total >= s:
                result = min(result, right-left+1)
                total -= nums[left]
                left += 1
        return result if result <= len(nums) else 0

    def minSubArrayLen2(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= s:
                left = self.find_left(left, right, nums, s, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    solu = Solution()
    s = 4
    nums = [2,3,1,2,4,3]
    res = solu.minSubArrayLen2(s, nums)
    print(res)
