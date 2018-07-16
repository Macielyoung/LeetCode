#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.outputTrees(1, n)

    def outputTrees(self, start, end):
        result = []
        if(start > end):
            return [None]

        if(start == end):
            result.append(TreeNode(start))
            return result

        for i in range(start, end+1):
            left = self.outputTrees(start, i-1)
            right = self.outputTrees(i+1, end)
            for j in range(len(left)):
                for k in range(len(right)):
                    root = TreeNode(i)
                    root.left = left[j]
                    root.right = right[k]
                    result.append(root)
        return result

if __name__ == '__main__':
    solu = Solution()
    res = solu.generateTrees(3)
    print res[0].right.val