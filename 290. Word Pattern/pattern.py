#-*- coding: UTF-8 -*-

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict = {}
        strings = str.split()
        if(len(strings) != len(pattern)):
            return False
        for i, j in zip(list(pattern), strings):
            if i not in dict:
                if j not in dict.values():
                    dict[i] = j
                else:
                    return False
            else:
                if(dict[i] != j):
                    return False
        return True

if __name__ == '__main__':
    solu = Solution()
    pattern = "abba"
    str = "dog dog dog dog"
    res = solu.wordPattern(pattern, str)
    print(res)