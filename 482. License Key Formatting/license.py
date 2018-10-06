#-*- coding: UTF-8 -*-

class Solution(object):
    # 分割字符串，使每段长度都小于或等于K，不足的可以合并，但不能超过长度K
    def splitString(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        strings = S.split('-')
        ss = strings[0]
        newString = []
        for i in range(1, len(strings)):
            if len(ss)+len(strings[i])<K:
                ss += strings[i]
            elif len(ss)+len(strings[i])==K:
                ss += strings[i]
                newString.append(ss)
                ss = ""
            else:
                newString.append(ss)
                ss = strings[i]
        return '-'.join(newString).upper()

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        strings = "".join(S.split('-')).upper()
        new = []
        while(len(strings)>=K):
            new.append(strings[-K:])
            strings = strings[:-K]
        if len(strings)>0:
            new.append(strings)
        new.reverse()
        return "-".join(new)

if __name__ == '__main__':
    solu = Solution()
    S = "2-4A0r7-4k"
    K = 4
    res = solu.licenseKeyFormatting(S, K)
    print(res)