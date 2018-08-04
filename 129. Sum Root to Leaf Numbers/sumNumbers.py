#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum(root, total, adding):
            if not root.left and not root.right:
                return total + (adding * 10 + root.val)
            if root.left:
                total = sum(root.left, total, adding * 10 + root.val)
            if root.right:
                total = sum(root.right, total, adding * 10 + root.val)
            return total
        if not root:
            return 0
        return sum(root, 0, 0)

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(4)
    B = TreeNode(9)
    C = TreeNode(0)
    D = TreeNode(5)
    E = TreeNode(1)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    res = solu.sumNumbers(A)
    print res
