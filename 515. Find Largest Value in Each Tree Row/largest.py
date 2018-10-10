#-*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = [root]
        res = []
        while any(nodes):
            nodes = [node for node in nodes if node]
            res.append(max([node.val for node in nodes]))
            nodes = [n for node in nodes for n in (node.left, node.right)]
        return res

    def largestValues2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 注意空树情况
        if not root:
            return []
        nodes = [(root, 0)]
        high_level = 0
        dict = {}
        while nodes:
            cur, h = nodes.pop(0)
            if h not in dict:
                dict[h] = [cur.val]
            else:
                dict[h].append(cur.val)
            if h > high_level:
                high_level = h
            if cur.left:
                nodes.append((cur.left, h + 1))
            if cur.right:
                nodes.append((cur.right, h + 1))
        res = [max(value) for value in dict.values()]
        return res

if __name__ == '__main__':
    solu = Solution()
    # A = TreeNode(1)
    # B = TreeNode(2)
    # C = TreeNode(3)
    # D = TreeNode(4)
    # E = TreeNode(5)
    # F = TreeNode(6)
    # G = TreeNode(7)
    # A.left = B
    # A.right = C
    # B.left = D
    # C.left = E
    # C.right = F
    # E.left = G

    A = TreeNode(1)
    B = TreeNode(3)
    C = TreeNode(2)
    D = TreeNode(5)
    E = TreeNode(3)
    F = TreeNode(9)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.right = F
    # res = solu.largestValues(A)
    res = solu.largestValues2(A)
    print(res)