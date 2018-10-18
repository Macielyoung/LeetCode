#-*- coding: UTF-8 -*-

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if s.count('A')>1:
            return False
        for i in range(len(s)-2):
            if s[i]=='L':
                if s[i+1]=='L' and s[i+2]=='L':
                    return False
        return True

    def checkRecord2(self, s):
        return False if 'LLL' in s or s.count('A') > 1 else True

if __name__ == '__main__':
    solu = Solution()
    s = 'PPALLL'
    res = solu.checkRecord2(s)
    print(res)