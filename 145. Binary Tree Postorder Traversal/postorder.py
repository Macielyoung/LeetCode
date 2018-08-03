#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.res.append(root.val)
        return self.res

    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        nodes = [root]
        while nodes:
            cur = nodes.pop()
            if cur != None:
                res.append(cur.val)
                nodes.append(cur.left)
                nodes.append(cur.right)
        res.reverse()
        return res

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(6)
    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    res = solu.postorderTraversal(A)
    res2 = solu.postorderTraversal2(A)
    print(res, res2)