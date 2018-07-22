#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def height(node, depth):
            if not node:
                return depth, True
            left_depth, left_balance = height(node.left, depth + 1)
            right_depth, right_balance = height(node.right, depth + 1)
            diff = abs(left_depth - right_depth)
            if diff > 1:
                return max(left_depth, right_depth), False
            return max(left_depth, right_depth), left_balance and right_balance
        height, balance = height(root, 0)
        return balance

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    F = TreeNode(5)
    G = TreeNode(10)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    D.left = F
    D.right = G
    balance = solu.isBalanced(A)
    print balance
