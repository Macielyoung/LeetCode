#-*- coding: UTF-8 -*-

class Solution(object):
    # 挨个判断s的元素是否在t中，如果在取最近的位置
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for val in s:
            if val in t:
                loc = t.index(val)
                t = t[loc+1:]
            else:
                return False
        return True

if __name__ == '__main__':
    solu = Solution()
    s = "abc"
    t = "ahbgdc"
    res = solu.isSubsequence(s, t)
    print(res)