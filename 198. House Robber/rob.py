#-*- coding: UTF-8 -*-

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = len(nums)
        if (num == 0):
            return 0
        if(num == 1):
            return nums[0]
        elif(num == 2):
            return max(nums[0], nums[1])
        else:
            dp = [0 for i in range(num+1)]
            dp[1] = nums[0]
            for i in range(2, num+1):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
            return dp[-1]

    def rob2(self, nums):
        # 使用交换技巧
        last, now = 0, 0
        for i in nums: last, now = now, max(last + i, now)
        return now

if __name__ == '__main__':
    solu = Solution()
    nums = [2,7,9,3,1]
    res = solu.rob(nums)
    res2 = solu.rob2(nums)
    print(res, res2)