#-*- coding: UTF-8 -*-

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

if __name__ == '__main__':
    solu = Solution()
    s = "A man, a plan, a canal: Panama"
    res = solu.reverseString(s)
    print(res)