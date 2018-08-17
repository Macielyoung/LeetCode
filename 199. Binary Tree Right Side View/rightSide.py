#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 遍历每层节点
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dict = {}
        nodes = [(root, 0)]
        res = []
        while nodes:
            cur, height = nodes.pop()
            if height not in dict:
                dict[height] = [cur]
            else:
                dict[height].append(cur)
            if cur.right:
                nodes.append((cur.right, height+1))
            if cur.left:
                nodes.append((cur.left, height+1))
        for level in dict.keys():
            res.append(dict[level][-1].val)
        return res

    def rightSideView2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        nodes = [(root, 0)]
        levels = []
        while nodes:
            cur, height = nodes.pop(0)
            if height not in levels:
                levels.append(height)
                res.append(cur.val)
            if cur.right:
                nodes.append((cur.right, height+1))
            if cur.left:
                nodes.append((cur.left, height+1))
        return res

    # DFS
    def rightSideView3(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        def dfs(node, level):
            if not node: return
            if level > len(view):
                view.append(node.val)
            if node.right:
                dfs(node.right, level+1)
            if node.left:
                dfs(node.left, level+1)
        dfs(root, 1)
        return view


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
    B.right = E
    C.right = D
    D.left = F
    res = solu.rightSideView3(A)
    print(res)