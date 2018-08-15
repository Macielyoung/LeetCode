#-*- coding: UTF-8 -*-

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        num = len(nums)
        if num == 1:
            return nums[0]
        elif num==2 or num == 3:
            return max(nums)
        else:
            dp = [[0, 0] for i in range(num)]
            dp[0][0] = 0
            dp[0][1] = nums[0]
            dp[1][0] = nums[1]
            dp[1][1] = nums[0]
            for i in range(2, num):
                dp[i][0] = max(dp[i-1][0], dp[i-2][0]+nums[i])
            for i in range(2, num-1):
                dp[i][1] = max(dp[i-1][1], dp[i-2][1]+nums[i])
            dp[num-1][1] = dp[num-2][1]
            return max(dp[-1][0], dp[-1][1])


if __name__ == '__main__':
    solu = Solution()
    nums = [1,2,3,1,5,10]
    res = solu.rob(nums)
    print(res)