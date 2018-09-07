#-*- coding: UTF-8 -*-

class Solution:
    def __init__(self):
        self.maxLen = 1
        self.sub = ""

    # 中心扩散法，时间复杂度O(n^2)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if(len(s)<=1):
            return s
        for i in range(len(s)-1):
            self.findlongest(s, i, i)
            self.findlongest(s, i, i+1)
        return self.sub

    def findlongest(self, s, low, high):
        while(low>=0 and high<=len(s)-1):
            if(s[low] == s[high]):
                if(high-low+1 > self.maxLen):
                    self.maxLen = high-low+1
                    self.sub = s[low:high+1]
                low -= 1
                high += 1
            else:
                break

if __name__ == '__main__':
    solu = Solution()
    s = "babad"
    res = solu.longestPalindrome(s)
    print(res)