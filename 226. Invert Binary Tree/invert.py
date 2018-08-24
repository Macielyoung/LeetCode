#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 递归
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.left and root.right:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root
        if root.left and root.right == None:
            left = self.invertTree(root.left)
            root.left = None
            root.right = left
            return root
        if root.right and root.left == None:
            right = self.invertTree(root.right)
            root.left = right
            root.right = None
            return root
        if root.left == None and root.right == None:
            return root

    # 非递归
    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        nodes = [root]
        while nodes:
            cur = nodes.pop()
            if cur.left and cur.right:
                nodes.append(cur.left)
                nodes.append(cur.right)
                cur.right, cur.left = cur.left, cur.right
                continue
            if cur.left and cur.right == None:
                nodes.append(cur.left)
                cur.left, cur.right = None, cur.left
                continue
            if cur.right and cur.left == None:
                nodes.append(cur.right)
                cur.left, cur.right = cur.right, None
                continue
        return root

    # 针对方法二的非递归简化了步骤
    def invertTree3(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        nodes = [root]
        while nodes:
            cur = nodes.pop()
            if cur:
                nodes.append(cur.left)
                nodes.append(cur.right)
                cur.right, cur.left = cur.left, cur.right
        return root


if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(4)
    B = TreeNode(2)
    C = TreeNode(7)
    D = TreeNode(1)
    E = TreeNode(3)
    F = TreeNode(6)
    G = TreeNode(9)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    res = solu.invertTree(A)
    print(res.left.val, res.left.left.val, res.right.val)

