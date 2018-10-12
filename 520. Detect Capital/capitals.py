#-*- coding: UTF-8 -*-

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if ord(word[0]) >=97 and ord(word[0]) <= 122:
            for i in range(1, len(word)):
                if ord(word[i]) < 97:
                    return False
        elif ord(word[0]) >= 65 and ord(word[0]) <= 90:
            if(n==1):
                return True
            if ord(word[1]) >=65 and ord(word[1]) <= 90:
                for i in range(2, len(word)):
                    if ord(word[i]) > 90:
                        return False
            elif ord(word[1]) >=97 and ord(word[1]) <= 122:
                for i in range(2, len(word)):
                    if ord(word[i]) < 97:
                        return False
        return True

    def detectCapitalUse2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() or word.isupper() or word.istitle()

if __name__ == '__main__':
    solu = Solution()
    word = "G"
    res = solu.detectCapitalUse(word)
    print(res)