#-*- coding: UTF-8 -*-

class Solution:
    # 思路正确，不过写法复杂了
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        flag = 0
        while(i<j):
            while(string[i] not in vowels):
                if(i<j):
                    i += 1
                else:
                    flag = 1
                    break
            if (flag):
                break
            while(string[j] not in vowels):
                if(i<j):
                    j -= 1
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return "".join(string)

    # 写法简洁
    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s) - 1
        while (i < j):
            if string[i] in vowels and string[j] in vowels:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
            elif string[i] not in vowels:
                i += 1
            elif string[j] not in vowels:
                j -= 1
        return "".join(string)


if __name__ == '__main__':
    solu = Solution()
    s = "leetcode"
    res = solu.reverseVowels2(s)
    print(res)