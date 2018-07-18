#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def addTolist(node, dep):
            if not node: return
            if dep>=len(res): res.append([])
            res[dep].append(node.val)
            if node.left:
                addTolist(node.left, dep+1)
            if node.right:
                addTolist(node.right, dep+1)
        addTolist(root, 0)
        res.reverse()
        return res

    def levelOrderBottom2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level, res = [root], [[root.val]]
        while level:
            cur = []
            node_in_next_level = 0
            for node in level:
                if(node.left or node.right) and not node_in_next_level:
                    res.append([])
                    node_in_next_level = 1
                if node.left:
                    cur.append(node.left)
                    res[-1].append(node.left.val)
                if node.right:
                    cur.append(node.right)
                    res[-1].append(node.right.val)
            level = cur
        return res[::-1]

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(3)
    B = TreeNode(9)
    C = TreeNode(20)
    D = TreeNode(15)
    E = TreeNode(7)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    res = solu.levelOrderBottom(A)
    print(res)