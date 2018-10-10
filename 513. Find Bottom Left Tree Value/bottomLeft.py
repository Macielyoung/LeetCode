#-*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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
                nodes.append((cur.left, h+1))
            if cur.right:
                nodes.append((cur.right, h+1))
        return dict[high_level][0]

    # 记住最后一层插入的节点即可
    def findBottomLeftValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodes = [root]
        while any(nodes):
            # 去除空节点
            nodes = [node for node in nodes if node]
            pre = nodes
            nodes = [n for node in nodes for n in (node.left, node.right)]
        return pre[0].val

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
    C.left = E
    C.right = F
    E.left = G
    res = solu.findBottomLeftValue2(A)
    print(res)