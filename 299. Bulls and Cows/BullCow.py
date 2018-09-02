#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        ls = []
        lg = []
        count1 = 0
        count2 = 0
        for i, j in zip(secret, guess):
            if(i==j):
                count1 += 1
            else:
                ls.append(i)
                lg.append(j)
        for i in ls:
            if(i in lg):
                lg.remove(i)
                count2 += 1
        hint = str(count1)+"A"+str(count2)+"B"
        return hint

    # 统计词频
    def getHint2(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = Counter(secret), Counter(guess)
        count1 = sum(i==j for i, j in zip(secret, guess))
        return "%sA%sB" % (count1, sum((s & g).values()) - count1)

if __name__ == '__main__':
    solu = Solution()
    secret = "1123"
    guess = "0111"
    res = solu.getHint2(secret, guess)
    print(res)
