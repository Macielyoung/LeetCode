#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursively
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0 and len(inorder)==0:
            return None
        #loc1 = -1
        root = TreeNode(preorder[0])
        # 查找索引位置，可以使用函数index
        # for i in range(len(inorder)):
        #     if inorder[i] == preorder[0]:
        #         loc1 = i
        #         break
        loc1 = inorder.index(preorder[0])
        left_in = inorder[:loc1]
        right_in = inorder[loc1+1:]
        left_pre = preorder[1:loc1+1]
        right_pre = preorder[loc1+1:]
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root

    # iteratively
    def buildTree2(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        stack, preorder, inorder = [], preorder[::-1], inorder[::-1]
        root = pre = TreeNode(-1)
        while preorder:
            while not stack or stack[-1].val != inorder[-1]:
                pre.left = pre = TreeNode(preorder.pop())
                stack.append(pre)
            while stack and stack[-1].val == inorder[-1]:
                pre = stack.pop()
                inorder.pop()
            if preorder:
                pre.right = pre = TreeNode(preorder.pop())
                stack.append(pre)
        return root.left

if __name__ == '__main__':
    solu = Solution()
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    root = solu.buildTree2(preorder, inorder)
    print root.val, root.left.val, root.right.val
