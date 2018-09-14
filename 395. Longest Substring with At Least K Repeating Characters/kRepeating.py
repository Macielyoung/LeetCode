#-*- coding: UTF-8 -*-
from collections import Counter

class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict = Counter(s)
        if all(dict[i]>=k for i in dict):
            return len(s)
        start, longest = 0, 0
        for i in xrange(len(s)):
            if dict[s[i]] < k:
                longest = max(longest, self.longestSubstring(s[start:i], k))
                start = i + 1
        longest = max(longest, self.longestSubstring(s[start:], k))
        return longest

    # recursively
    def longestSubstring2(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(z, k) for z in s.split(c))
        return len(s)

    # iteratively
    def longestSubstring3(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        stack = []
        stack.append(s)
        ans = 0
        while stack:
            s = stack.pop()
            for c in set(s):
                if s.count(c) < k:
                    stack.extend([z for z in s.split(c)])
                    break
            else:
                ans = max(ans, len(s))
        return ans


if __name__ == '__main__':
    solu = Solution()
    s = "aaabbcsddsaabebcs"
    k = 3
    res = solu.longestSubstring2(s, k)
    print(res)

