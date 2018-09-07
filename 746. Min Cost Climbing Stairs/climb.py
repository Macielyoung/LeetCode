#-*- coding: UTF-8 -*-

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        n = len(cost)
        dp = [0 for i in range(n+1)]
        # dp[0], dp[1] = cost[0], min(cost[0], cost[1])
        for i in range(2, n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

if __name__ == '__main__':
    solu = Solution()
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    res = solu.minCostClimbingStairs(cost)
    print(res)