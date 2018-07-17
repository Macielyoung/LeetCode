#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     return self.check_bst(root, float("-inf"), float("inf"))
    #
    # def check_bst(self, node, left, right):
    #     if not node:
    #         return True
    #
    #     if not left < node.val < right:
    #         return False
    #
    #     return (self.check_bst(node.left, left, node.val)
    #             and self.check_bst(node.right, node.val, right))

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root is None):
            return True
        if(root.left is None and root.right is None):
            return True
        nums = []
        self.inorder(root, nums)
        prev = nums[0]
        for i in range(1, len(nums)):
            if(prev >= nums[i]):
                return False
            prev = nums[i]
        return True

    def inorder(self, root, nums):
        if(root is None):
            return
        self.inorder(root.left, nums)
        nums.append(root.val)
        self.inorder(root.right, nums)

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(10)
    B = TreeNode(5)
    C = TreeNode(15)
    D = TreeNode(6)
    E = TreeNode(20)
    A.left = B
    A.right = C
    C.left = D
    C.right = E
    bres = solu.isValidBST(A)
    print(bres)
