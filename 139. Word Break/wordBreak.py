#-*- coding: UTF-8 -*-

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not s:
            return True
        num = len(s) + 1
        dp = [False] * num
        dp[0] = True
        for i in range(1, num):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
                    break
        return dp[-1]

if __name__ == "__main__":
    solu = Solution()
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    res = solu.wordBreak(s, wordDict)
    print(res)
