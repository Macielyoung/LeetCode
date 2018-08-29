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
        if root in (None, p, q):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 都不为空，说明左右子树都有目标节点，公共祖先就是root本身
        # 若一个为空，说明在一侧子树上。
        return root if left and right else left or right

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(5)
    C = TreeNode(1)
    D = TreeNode(6)
    E = TreeNode(2)
    F = TreeNode(0)
    G = TreeNode(8)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    res = solu.lowestCommonAncestor(A, D, E)
    print(res.val)