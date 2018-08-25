#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(6)
    B = TreeNode(2)
    C = TreeNode(8)
    D = TreeNode(0)
    E = TreeNode(4)
    F = TreeNode(7)
    G = TreeNode(9)
    H = TreeNode(3)
    I = TreeNode(5)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    E.left = H
    E.right = I
    p, q = B, C
    res = solu.lowestCommonAncestor(A, p, q)
    print res.val