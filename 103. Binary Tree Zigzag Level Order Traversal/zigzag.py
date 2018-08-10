#-*- coding: UTF-8 -*-
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        values = defaultdict(list)
        while queue:
            cur, height = queue.pop(0)
            values[height].append(cur.val)
            if cur.left:
                queue.append((cur.left, height+1))
            if cur.right:
                queue.append((cur.right, height+1))
        res = []
        iter = True
        for i in values:
            if iter:
                res.append(values[i])
                iter = False
            else:
                res.append(values[i][::-1])
                iter = True
        return res

    def zigzagLevelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes = [(root, 0)]
        res = []
        row = []
        count = 0
        num = 1
        while nodes:
            cur, height = nodes.pop(0)
            count += 1
            row.append(cur.val)
            if (cur.left):
                nodes.append((cur.left, height + 1))
            if (cur.right):
                nodes.append((cur.right, height + 1))
            if (count == num):
                num = len(nodes)
                count = 0
                if height%2 == 0:
                    res.append(row)
                else:
                    res.append(row[::-1])
                row = []
        return res

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    F= TreeNode(1)
    G = TreeNode(2)
    A.left = B
    A.right = C
    B.left = F
    B.right = G
    C.left = D
    C.right = E
    res = solu.zigzagLevelOrder(A)
    print(res)