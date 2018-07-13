#-*- coding: UTF-8 -*-

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(s[0]=='0'): return 0
        num = len(s)
        dp = [0]*(num+1)
        dp[0] = dp[1] = 1
        for i in range(1, num):
            first = int(s[i:i+1])
            second = int(s[i-1:i+1])
            if 0<first<=9:
                dp[i+1] = dp[i]
            if 10<=second<=26:
                dp[i+1] += dp[i-1]
            if dp[i+1] == 0:
                return 0
        return dp[num]

if __name__ == '__main__':
    solu = Solution()
    s = "10"
    count = solu.numDecodings(s)
    print(count)
