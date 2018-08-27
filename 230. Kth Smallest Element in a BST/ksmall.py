#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 比较进入子树
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def countLeft(node):
            count = 0
            if node.left:
                nodes = [node.left]
                while nodes:
                    cur = nodes.pop()
                    count += 1
                    if cur.left:
                        nodes.append(cur.left)
                    if cur.right:
                        nodes.append(cur.right)
            return count
        left_num = countLeft(root)
        if(k == left_num+1):
            return root.val
        elif(k <= left_num):
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k-left_num-1)

    # 中序遍历求k-1个元素
    def kthSmallest2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def helper(node, res):
            if node:
                helper(node.left, res)
                res.append(node.val)
                helper(node.right, res)
        if not root:
            return None
        res = []
        helper(root, res)
        return res[k-1]

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(8)
    B = TreeNode(4)
    C = TreeNode(10)
    D = TreeNode(2)
    E = TreeNode(6)
    F = TreeNode(1)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    D.left = F
    k = 4
    res = solu.kthSmallest2(A, k)
    print(res)