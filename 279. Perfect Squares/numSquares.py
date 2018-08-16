#-*- coding: UTF-8 -*-

class Solution:
    # DP
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf') for i in range(n+1)]
        for i in range(1, int(n**0.5)+1):
            dp[i*i] = 1
        for i in range(1, n+1):
            for k in range(1, int(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-k*k]+1)
        return dp[-1]

    # BFS
    def numSquares2(self, n):
        if n == 1: return 1
        check = {n}
        ans = 0
        while 0 not in check:
            child = set()
            for x in check:
                for i in range(1, int(x**0.5) + 1):
                    child.add(x - i ** 2)
            check = child
            ans += 1
        return ans

if __name__ == '__main__':
    solu = Solution()
    n = 12
    res = solu.numSquares2(n)
    print res