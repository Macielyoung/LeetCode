#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left==None and root.right==None:
            if sum == root.val:
                return True
            else:
                return False
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return (left or right)

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(5)
    B = TreeNode(4)
    C = TreeNode(8)
    D = TreeNode(11)
    E = TreeNode(13)
    F = TreeNode(4)
    G = TreeNode(7)
    H = TreeNode(2)
    I = TreeNode(1)
    A.left = B
    A.right = C
    B.left = D
    C.left = E
    C.right = F
    D.left = G
    D.right = H
    F.right = I
    X = TreeNode(1)
    Y = TreeNode(2)
    X.left = Y
    existence = solu.hasPathSum(X, 1)
    print existence