#-*- coding: UTF-8 -*-
import math

class Solution(object):
    # 想的简单了，不是一直考虑最差情况
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        num = int(math.log(n, 2))
        sum = 0
        while(num):
            mid = (left+right)/2+1
            sum += mid
            left = mid+1
            num -= 1
        return sum

    # 使用动归
    def getMoneyAmount2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n + 1) for i in range(n + 1)]

        for length in range(2, n + 1):
            for start_ind in range(1, n + 1 - length + 1):
                end_ind = start_ind + length - 1
                dp[start_ind][end_ind] = min(start_ind + dp[start_ind + 1][end_ind], end_ind + dp[start_ind][end_ind - 1])
                for k in range(start_ind + 1, end_ind):
                    dp[start_ind][end_ind] = min(dp[start_ind][end_ind], k + max(dp[start_ind][k - 1], dp[k + 1][end_ind]))

        return dp[1][n]

if __name__ == '__main__':
    solu = Solution()
    n = 4
    res = solu.getMoneyAmount2(n)
    print(res)