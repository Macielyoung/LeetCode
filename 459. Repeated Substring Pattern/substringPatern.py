#-*- coding: UTF-8 -*-

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n/2+1):
            substring = s[:i]*(n/i)
            if(s == substring):
                return True
        return False

    def repeatedSubstringPattern2(self, s):
        return s in (s + s)[1:-1]

if __name__ == '__main__':
    solu = Solution()
    s = "abc"
    res = solu.repeatedSubstringPattern2(s)
    print(res)