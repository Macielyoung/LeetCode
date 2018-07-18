#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.depth = 0

class Solution:
    # recursive
    # def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if(not root):
    #         return 0
    #     depth = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    #     return depth

    # Non-recursive, using stack
    def maxDepth(self, root):
        if root is None:
            return 0
        max_depth = 1
        root.depth = 1
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left is None and node.right is None:
                max_depth = max(node.depth, max_depth)
            if node.left is not None:
                node.left.depth = node.depth + 1
                stack.append(node.left)
            if node.right is not None:
                node.right.depth = node.depth + 1
                stack.append(node.right)
        return max_depth

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    depth = solu.maxDepth(A)
    print(depth)