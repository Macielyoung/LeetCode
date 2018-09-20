#-*- coding: UTF-8 -*-

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

if __name__ == '__main__':
    solu = Solution()
    s = "Hello, my name is John"
    res = solu.countSegments(s)
    print(res)