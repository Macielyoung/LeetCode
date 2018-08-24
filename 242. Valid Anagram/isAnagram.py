#-*- coding: UTF-8 -*-
from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = Counter(s)
        t1 = Counter(t)
        return True if s1==t1 else False

if __name__ == '__main__':
    solu = Solution()
    s = "rat"
    t = "car"
    res = solu.isAnagram(s, t)
    print(res)