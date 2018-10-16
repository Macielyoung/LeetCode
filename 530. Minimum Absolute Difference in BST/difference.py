#-*- coding: UTF-8 -*-
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 任意两节点最小差值
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [(root, 0)]
        values = []
        while nodes:
            cur, h = nodes.pop()
            values.append(cur.val)
            if cur.left:
                nodes.append((cur.left, h+1))
            if cur.right:
                nodes.append((cur.right, h+1))
        values.sort()
        new = [values[i+1]-values[i] for i in range(len(values)-1)]
        res = min(new)
        return res

    # 利用二叉搜索树的特性，使用中序遍历
    def getMinimumDifference2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = []
        def inorder(node):
            if node.left:
                inorder(node.left)
            nodes.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return min(abs(a-b) for a,b in zip(nodes, nodes[1:]))

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(17)
    B = TreeNode(5)
    C = TreeNode(35)
    D = TreeNode(1)
    E = TreeNode(10)
    F = TreeNode(24)
    G = TreeNode(36)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    C.right = G
    res = solu.getMinimumDifference2(A)
    print(res)