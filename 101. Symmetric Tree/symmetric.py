#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = self.downward(root.left, root.right)
        return res

    def downward(self, left, right):
        if left and right:
            return left.val == right.val and self.downward(left.left, right.right) and self.downward(left.right, right.left)
        return left == right



if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(2)
    D = TreeNode(3)
    E = TreeNode(3)
    F = TreeNode(4)
    G = TreeNode(4)
    A.left = B
    A.right = C
    B.left = D
    # B.right = F
    # C.left = G
    C.left = E
    ans = solu.isSymmetric(A)
    print ans