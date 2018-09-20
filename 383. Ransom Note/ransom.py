#-*- coding: UTF-8 -*-

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazines = list(magazine)
        for val in ransomNote:
            if val in magazines:
                magazines.remove(val)
            else:
                return False
        return True

if __name__ == '__main__':
    solu = Solution()
    ransomNote = "fffbfg"
    magazine = "effjfggbffjdgbjjhhdegh"
    res = solu.canConstruct(ransomNote, magazine)
    print(res)