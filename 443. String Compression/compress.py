#-*- coding: UTF-8 -*-

class Solution(object):
    # 需要针对chars来修改
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        cursor = chars[0]
        maxlen = 1
        n = len(chars)
        for i in range(1, n):
            if chars[i] == cursor:
                maxlen += 1
            else:
                if maxlen > 1:
                    chars.append(cursor)
                    chars += list(str(maxlen))
                else:
                    chars.append(cursor)
                cursor = chars[i]
                maxlen = 1
        if maxlen > 1:
            chars.append(cursor)
            chars += list(str(maxlen))
        else:
            chars.append(cursor)
        chars = chars[n:]
        return chars

    def compress2(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

if __name__ == '__main__':
    solu = Solution()
    chars = ["a","a","b","b","c","c","c"]
    res = solu.compress2(chars)
    print(res)