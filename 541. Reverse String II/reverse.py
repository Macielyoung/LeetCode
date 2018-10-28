#-*- coding: UTF-8 -*-

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        slist = list(s)
        i, n = 0, len(s)
        while i < n:
            if i+k<n:
                slist[i:i+k] = slist[i:i+k][::-1]
            else:
                slist[i:] = slist[i:][::-1]
            i += 2*k
        string = "".join(slist)
        return string

if __name__ == '__main__':
    solu = Solution()
    s = "abcdefg"
    k = 2
    res = solu.reverseStr(s, k)
    print(res)