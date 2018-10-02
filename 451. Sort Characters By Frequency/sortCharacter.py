#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = Counter(s)
        chars = sorted(dict.items(), key = lambda x:x[1], reverse=True)
        res = ""
        # 也可以使用join函数来合并字符串
        for pair in chars:
            c, v = pair[0], pair[1]
            res += c*v
        return res

if __name__ == '__main__':
    solu = Solution()
    s = "tree"
    res = solu.frequencySort(s)
    print(res)