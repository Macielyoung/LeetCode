#-*- coding: UTF-8 -*-

class Solution:
    # 更快
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}
        char_dict2 = {}
        for i, j in zip(s, t):
            if i not in char_dict:
                char_dict[i] = j
            else:
                if j != char_dict[i]:
                    return False
            if j not in char_dict2:
                char_dict2[j] = i
            else:
                if i != char_dict2[j]:
                    return False
        return True

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char_dict = {}
        for i, j in zip(s, t):
            if i not in char_dict:
                if j in char_dict.values():
                    return False
                char_dict[i] = j
            else:
                if j != char_dict[i]:
                    return False
        return True

if __name__ == '__main__':
    solu = Solution()
    s = "egg"
    t = "add"
    res = solu.isIsomorphic(s, t)
    print(res)
