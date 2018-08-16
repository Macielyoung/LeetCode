#-*- coding: UTF-8 -*-

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if(nums[i] > nums[j]):
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
        return max(dp)

if __name__ == '__main__':
    solu = Solution()
    nums = [2]
    res = solu.lengthOfLIS(nums)
    print(res)