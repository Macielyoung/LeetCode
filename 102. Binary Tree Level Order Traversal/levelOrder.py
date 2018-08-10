#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        # ans.append([root.val])
        nodes = [root]
        while(nodes):
            res = []
            num = len(nodes)
            for ele in nodes:
                res.append(ele.val)
            ans.append(res)
            for i in range(num):
                if nodes[i].left:
                    nodes.append(nodes[i].left)
                if nodes[i].right:
                    nodes.append(nodes[i].right)
            del nodes[:num]
        return ans

    def levelOrder2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans = []
        nodes = [root]
        while (nodes):
            res = []
            num = len(nodes)
            for i in range(num):
                ele = nodes.pop(0)
                res.append(ele.val)
                if ele.left:
                    nodes.append(ele.left)
                if ele.right:
                    nodes.append(ele.right)
            ans.append(res)
        return ans



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
    ans = solu.levelOrder2(A)
    print ans

