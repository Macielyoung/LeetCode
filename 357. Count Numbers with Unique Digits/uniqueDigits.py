#-*- coding: UTF-8 -*-

class Solution(object):
    # 递推
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res, j = 9, 9
        for i in range(n-1):
            res *= j
            j -= 1
        return res + self.countNumbersWithUniqueDigits(n-1)

    # 动归
    def countNumbersWithUniqueDigits2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 1
        dp = [0] * (n + 1)
        dp_2 = [0] * (n + 1)
        dp[1] = 9
        dp_2[1] = 1
        for i in range(2, n + 1):
            if i <= 9:
                dp[i] += (10 - i) * dp[i - 1]
            if i <= 10:
                dp_2[i] += (11 - i) * dp_2[i - 1]
                dp_2[i] += (11 - i) * dp[i - 2]
        return sum(dp) + sum(dp_2)

if __name__ == '__main__':
    solu = Solution()
    n = 4
    res = solu.countNumbersWithUniqueDigits2(n)
    print(res)