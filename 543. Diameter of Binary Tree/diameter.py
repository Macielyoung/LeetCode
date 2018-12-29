#-*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1
        self.height(root)
        return self.res - 1

    def height(self, node):
        if not node:
            return 0
        l, r = self.height(node.left), self.height(node.right)
        self.res = max(self.res, l+r+1)
        return max(l, r) + 1

if __name__ == '__main__':
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    solu = Solution()
    res = solu.diameterOfBinaryTree(A)
    print(res)
