#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return
        # new_root = root
        # nodes = [root]
        # while nodes:
        #     ele = nodes.pop(0)
        #     new_root = TreeNode(ele.val)
        #     while ele.left:
        #         new_root.right = TreeNode(ele.left.val)
        #         new_root = new_root.right
        #         ele = ele.left
        #     if ele.right:
        #         new_root.right =

        if not root:
            return
        res = []
        self.inorder(root, res)
        new_root = recur = TreeNode(res[0])
        for i in range(1, len(res)):
            recur.right = TreeNode(res[i])
            recur = recur.right
        return new_root

    def inorder(self, node, res):
        if not node:
            return None
        res.append(node.val)
        self.inorder(node.left, res)
        self.inorder(node.right, res)

    def flatten2(self, root):
        while root:
            if root.left:
                end = root.left
                while end.right:
                    end = end.right

                end.right = root.right
                root.right = root.left
                root.left = None

            root = root.right

    def flatten3(self, node):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        curr = node
        while stack or curr:
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                curr.right = curr.left
                curr.left = None
                curr = curr.right
            elif stack:
                curr.right = stack.pop()
                curr = curr.right
            else:
                curr = None

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    A.left = B
    A.right = E
    B.left = C
    B.right = D
    E.right = F
    root = solu.flatten2(A)
    print root.val