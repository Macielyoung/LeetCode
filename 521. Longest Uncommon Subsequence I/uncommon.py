#-*- coding: UTF-8 -*-

class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if len(a) != len(b):
            return max(len(a), len(b))
        if a == b:
            return -1
        else:
            return len(a)

if __name__ == '__main__':
    solu = Solution()
    a = "asfas"
    b = "asf"
    res = solu.findLUSlength(a, b)
    print(res)