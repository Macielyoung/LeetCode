#-*- coding: UTF-8 -*-

class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        if(n<k):
            return ans
        self.helper(n, k, 1, [], ans)
        return ans

    def helper(self, n, k, start, res, ans):
        if not k:
            ans.append(res)
            return
        for i in range(start, n+1):
            self.helper(n, k-1, i+1, res+[i], ans)

if __name__ == '__main__':
    solu = Solution()
    ans = solu.combine(4, 2)
    print(ans)