#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.res = []

    # 递归
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.res.append(root.val)
        if root.left:
            self.preorderTraversal(root.left)
        if root.right:
            self.preorderTraversal(root.right)
        return self.res

    # 迭代
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        nodes = []
        nodes.append(root)
        while nodes:
            cur = nodes.pop()
            if(cur != None):
                res.append(cur.val)
                nodes.append(cur.right)
                nodes.append(cur.left)
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
    res = solu.preorderTraversal(A)
    res2 = solu.preorderTraversal2(A)
    print(res, res2)