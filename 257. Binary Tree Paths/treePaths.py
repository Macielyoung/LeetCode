#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []

        def dfs(current_node, path):

            if not current_node:
                return []
            if not current_node.left and not current_node.right:
                path = path + [current_node.val]
                paths.append("->".join(map(str, path)))
                return

            path = path + [current_node.val]
            dfs(current_node.left, path)
            dfs(current_node.right, path)

        dfs(root, paths)
        return paths

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
    B.right = E
    C.left = F
    C.right = G
    res = solu.binaryTreePaths(A)
    print(res)