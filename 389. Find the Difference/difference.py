#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    # 统计词频
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s1, t1 = Counter(s), Counter(t)
        inter = t1 - s1
        return "".join(inter.keys())

    # 排序后比较元素
    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        for i in range(len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]

    # 使用异或操作得出单个的字符
    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

if __name__ == '__main__':
    solu = Solution()
    s = "abcda"
    t = "abcde"
    res = solu.findTheDifference(s, t)
    ss = list(Counter(s))
    print(ss)
    print(res)
