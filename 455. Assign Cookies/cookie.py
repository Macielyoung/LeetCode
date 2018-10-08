#-*- coding: UTF-8 -*-

class Solution(object):
    # 时间复杂度：O(nlogn)
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        i, j = 0, 0
        m, n = len(g), len(s)
        while i<m and j<n:
            if(s[j]>=g[i]):
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        return count
        #可以选择只迭代cookie即可
        # g.sort()
        # s.sort()
        # n = 0
        # for i in s:
        #     if n < len(g) and i >= g[n]:
        #         n += 1
        # return n

    def findContentChildren2(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        ans = 0
        while g and s:
            if s[0] >= g[0]:
                ans += 1
                g.pop(0)
            s.pop(0)
        return ans

if __name__ == '__main__':
    solu = Solution()
    g = [1,2]
    s = [1,2,3]
    res = solu.findContentChildren2(g, s)
    print(res)