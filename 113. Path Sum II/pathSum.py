#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        vals = [root.val]
        if not root.left and not root.right:
            if(root.val == sum):
                return [[root.val]]
            else:
                return []
        if root.left:
            self.dfs(root.left, root.val, vals, sum)
        if root.right:
            self.dfs(root.right, root.val, vals, sum)
        return self.ans

    def dfs(self, root, total, vals, sum):
        total += root.val
        if not root.left and not root.right:
            if(total == sum):
                vals_root = vals + [root.val]
                self.ans.append(vals_root)
            else:
                return
        if root.left:
            vals_left = vals + [root.val]
            self.dfs(root.left, total, vals_left, sum)
        if root.right:
            vals_right = vals + [root.val]
            self.dfs(root.right, total, vals_right, sum)


if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(5)
    B = TreeNode(4)
    C = TreeNode(8)
    A.left = B
    A.right = C

    D = TreeNode(11)
    B.left = D

    E = TreeNode(13)
    F = TreeNode(4)
    C.left = E
    C.right = F

    G = TreeNode(7)
    H = TreeNode(2)
    D.left = G
    D.right = H

    I = TreeNode(5)
    J = TreeNode(1)
    F.left = I
    F.right = J
    ans = solu.pathSum(A, 22)
    print ans