#-*- coding: UTF-8 -*-

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        loc = inorder.index(postorder[-1])
        left_in = inorder[:loc]
        right_in = inorder[loc+1:]
        left_post = postorder[:loc]
        right_post = postorder[loc:-1]
        root.left = self.buildTree(left_in, left_post)
        root.right = self.buildTree(right_in, right_post)
        return root

    def buildTree2(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        stack = [root]
        i, j = len(postorder)-2, len(inorder)-1
        while i >= 0:
            node = TreeNode(postorder[i])
            tmp = None
            while stack and stack[-1].val == inorder[j]:
                tmp = stack.pop()
                j -= 1
            if tmp:
                tmp.left = node
            else:
                stack[-1].right = node
            stack.append(node)
            i -= 1
        return root

if __name__ == "__main__":
    solu = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = solu.buildTree(inorder, postorder)
    root2 = solu.buildTree2(inorder, postorder)
    print(root.val, root.left.val, root.right.val)
    print(root2.val, root2.left.val, root2.right.val)