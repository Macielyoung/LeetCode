#-*- coding: UTF-8 -*-
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = map(self.minDepth, (root.left, root.right))
        return 1+(min(height) or max(height))

    def minDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        d, D = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (d or D)

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    F = TreeNode(2)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    # B.left = F
    height = solu.minDepth(A)
    height2 = solu.minDepth2(A)
    print height, height2