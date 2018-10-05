#-*- coding: UTF-8 -*-

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = {}

        def find(i, j):
            if (i, j) not in dp:
                if i == j:
                    return nums[i]
                dp[i, j] = max(nums[i] - find(i + 1, j), nums[j] - find(i, j - 1))
            return dp[i, j]

        return find(0, len(nums) - 1) >= 0

    def PredictTheWinner2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 == 0:
            return True
        dp = list(nums)
        for j in xrange(1, len(nums)):
            for i in xrange(len(nums) - j):
                dp[i] = max(nums[i] - dp[i + 1], nums[i + j] - dp[i])
        return dp[0] >= 0

    def PredictTheWinner3(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = {}

        def helper(_sum, nums, start, end):

            if (start, end) in memo:
                return memo[(start, end)]

            if start == end:
                memo[(start, end)] = nums[start]
                return nums[start]

            score1 = _sum - helper(_sum - nums[start], nums, start + 1, end)
            score2 = _sum - helper(_sum - nums[end], nums, start, end - 1)

            res = max(score1, score2)
            memo[(start, end)] = res

            return res

        return helper(sum(nums), nums, 0, len(nums) - 1) * 2 >= sum(nums)

if __name__ == '__main__':
    solu = Solution()
    nums = [1, 210, 200, 7, 10]
    res = solu.PredictTheWinner3(nums)
    print(res)