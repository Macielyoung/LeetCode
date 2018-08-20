#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.i = 0
        self.vals = []
        nodes = []
        if root != None:
            nodes.append(root)
        while nodes:
            cur = nodes.pop()
            self.vals.append(cur.val)
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        self.vals.sort()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.vals)

    def next(self):
        """
        :rtype: int
        """
        val = self.vals[self.i]
        self.i += 1
        return val


if __name__ == '__main__':
    A = TreeNode(4)
    B = TreeNode(2)
    C = TreeNode(6)
    D = TreeNode(1)
    E = TreeNode(3)
    F = TreeNode(5)
    G = TreeNode(7)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    i = BSTIterator(A)
    res = []
    while i.hasNext():
        res.append(i.next())
    print(res)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())