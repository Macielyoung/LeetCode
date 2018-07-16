#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 卡特兰数
        if(n<0): return 0
        catlan = [0]*(n+1)
        catlan[0] = 1
        catlan[1] = 1
        for i in range(2,n+1):
            for j in range(i):
                catlan[i] += catlan[j]*catlan[i-j-1]
        return catlan[n]

if __name__ == '__main__':
    solu = Solution()
    n = 3
    res = solu.numTrees(n)
    print(res)
