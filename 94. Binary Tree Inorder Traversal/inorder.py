#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self):
    #     self.output = []
    #
    # def inorderTraversal(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     if(root == None):
    #         return []
    #     self.inorderTraversal(root.left)
    #     self.output.append(root.val)
    #     self.inorderTraversal(root.right)
    #     return self.output

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    G = TreeNode(7)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    out = solu.inorderTraversal(A)
    print(out)
