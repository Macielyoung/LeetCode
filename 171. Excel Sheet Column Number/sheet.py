#-*- coding: UTF-8 -*-

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = len(s)
        sum = 0
        for i in range(num):
            chr = s[i]
            sum += (ord(chr) - 64) * pow(26, num-1-i)
        return sum

    def titleToNumber2(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for chr in list(s):
            x = ord(chr)-64
            sum = sum*26+x
        return sum

if __name__ == '__main__':
    solu = Solution()
    s = 'ZYYY'
    res = solu.titleToNumber(s)
    res2 = solu.titleToNumber2(s)
    print(res, res2)