#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursive
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left==None and root.right==None:
            if sum == root.val:
                return True
            else:
                return False
        left = self.hasPathSum(root.left, sum - root.val)
        right = self.hasPathSum(root.right, sum - root.val)
        return (left or right)

    # non-recursive
    def hasPathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False

        # One queue to maintain Nodes
        # Second to maintain sum upto that node
        q1 = []
        q2 = []

        q1.append(root)
        q2.append(root.val)

        while (q1):

            ql = len(q1)
            for i in range(0, ql):

                a = q1.pop(0)
                b = q2.pop(0)

                # If node sum is equal to sum and is a leaf node then return True
                if (b == sum and a.left == None and a.right == None):
                    return True

                if (a.left != None):
                    q1.append(a.left)
                    q2.append(b + a.left.val)

                if (a.right != None):
                    q1.append(a.right)
                    q2.append(b + a.right.val)

        return False

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(5)
    B = TreeNode(4)
    C = TreeNode(8)
    D = TreeNode(11)
    E = TreeNode(13)
    F = TreeNode(4)
    G = TreeNode(7)
    H = TreeNode(2)
    I = TreeNode(1)
    A.left = B
    A.right = C
    B.left = D
    C.left = E
    C.right = F
    D.left = G
    D.right = H
    F.right = I
    X = TreeNode(1)
    Y = TreeNode(2)
    X.left = Y
    existence = solu.hasPathSum2(A, 22)
    print existence