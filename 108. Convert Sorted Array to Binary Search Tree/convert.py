#-*- coding: UTF-8 -*-
import math

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        num = len(nums)-1
        root = self.createTree(0, num, nums)
        return root

    def createTree(self, low, high, nums):
        if (low == high):
            root = TreeNode(nums[low])
            return root
        if (low < high):
            mid = math.ceil((low + high) / 2)
            # print(mid)
            root = TreeNode(nums[mid])
            root.left = self.createTree(low, mid-1, nums)
            root.right = self.createTree(mid+1, high, nums)
            return root

if __name__ == '__main__':
    solu = Solution()
    nums = [-10,-3,0,5,9]
    root = solu.sortedArrayToBST(nums)
    print(root.val, root.left.val, root.right.val, root.left.left.val, root.right.left.val)

