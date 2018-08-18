#-*- coding: UTF-8 -*-

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) <= 10:
            return []
        num = len(s)
        res1 = set()
        res2 = set()
        for i in range(num-9):
            key = s[i:i+10]
            if key not in res1:
                res1.add(key)
            else:
                res2.add(key)
        return list(res2)

if __name__ == '__main__':
    solu = Solution()
    s = "AAAAAAAAAAAAAAAA"
    res = solu.findRepeatedDnaSequences(s)
    print(res)