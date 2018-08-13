#-*- coding: UTF-8 -*-
import sys

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

    def minDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if(root.left==None and root.right==None): return 1
        left, right = 0, 0
        if(root.left != None):
            left = self.minDepth3(root.left)
        else:
            left = sys.maxsize
        if (root.right != None):
            right = self.minDepth3(root.right)
        else:
            right = sys.maxsize
        return min(left, right) + 1

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
    # height = solu.minDepth(A)
    # height2 = solu.minDepth2(A)
    height3 = solu.minDepth3(A)
    # print(height, height2, height3)
    print(height3)