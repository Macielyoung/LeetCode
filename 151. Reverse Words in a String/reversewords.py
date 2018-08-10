#-*- coding: UTF-8 -*-

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = [ i for i in s.split(' ') if i != '']
        if len(arr) == 0:
            return ""
        nstr = ""
        for val in arr[::-1]:
            nstr += val + ' '
        return nstr[:-1]

    def reverseWords2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    solu = Solution()
    s = "asd dsf asda waeda "
    res = solu.reverseWords2(s)
    print(res)