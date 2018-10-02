#-*- coding: UTF-8 -*-

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if not words:
            return []
        dict = {'q':1, 'w':1, 'e':1, 'r':1, 't':1, 'y':1, 'u':1, 'i':1, 'o':1, 'p':1,
                'a':2, 's':2, 'd':2, 'f':2, 'g':2, 'h':2, 'j':2, 'k':2, 'l':2,
                'z':3, 'x':3, 'c':3, 'v':3, 'b':3, 'n':3, 'm':3}
        res = []
        for i in range(len(words)):
            word = set(words[i].lower())
            mapping = []
            for val in word:
                mapping.append(dict[val])
            if(len(set(mapping))==1):
                res.append(words[i])
        return res

if __name__ == '__main__':
    solu = Solution()
    words = ["Hello", "Alaska", "Dad", "Peace"]
    res = solu.findWords(words)
    print(res)