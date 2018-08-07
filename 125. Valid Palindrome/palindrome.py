#-*- coding: UTF-8 -*-
import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        num = len(s)
        i = 0
        j = num - 1
        while ((j - i) >= 1):
            if not (s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z' or s[i] >= '0' and s[i] <= '9'):
                i += 1
                continue
            if not (s[j] >= 'a' and s[j] <= 'z' or s[j] >= 'A' and s[j] <= 'Z' or s[j] >= '0' and s[j] <= '9'):
                j -= 1
                continue
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 使用库函数
        string = [ch.lower() for ch in s if ch.isalnum()]
        print(string)
        return string[:]==string[::-1]


if __name__ == "__main__":
    solu = Solution()
    s = "A man, a plan, a canal: Panama"
    s1 = "0P"
    res = solu.isPalindrome2(s)
    print(res)