#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    # 时间复杂度高
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s)==1): return 0
        for i in range(len(s)):
            if (i!=len(s)-1):
                if s[i] not in s[:i]+s[i+1:]:
                    return i
            else:
                if s[i] not in s[:i]:
                    return i
        return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict = Counter(s)
        # indexs = [s.index(key) for key, value in dict.items() if value == 1]
        # return -1 if not indexs else min(indexs)

        # 可以不用Counter包，直接使用count函数来统计元素
        letters = 'abcdefghijklmnopqrstuvwxyz'
        indexs = [s.index(l) for l in letters if s.count(l)==1]
        return min(indexs) if len(indexs)>0 else -1


if __name__ == '__main__':
    solu = Solution()
    s = "dddccdbbaa"
    res = solu.firstUniqChar(s)
    res2 = solu.firstUniqChar2(s)
    print(res, res2)