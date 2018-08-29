#-*- coding: UTF-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 超时
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        nodes = [root]
        count = 0
        while nodes:
            cur = nodes.pop()
            count += 1
            if cur.left:
                nodes.append(cur.left)
            if cur.right:
                nodes.append(cur.right)
        return count

    def countNodes2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        height = 1
        cur = root
        while cur.left:
            height += 1
            cur = cur.left
        count = 2 ** height - 1
        if height > 1:
            nodes = [(root, 1)]
            while nodes:
                cur, h = nodes.pop()
                if(h != height-1):
                    nodes.append((cur.left, h+1))
                    nodes.append((cur.right, h+1))
                else:
                    if cur.left == None:
                        count -= 1
                    if cur.right == None:
                        count -= 1
        return count

    def countNodes3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        cur = root
        while cur:
            leftH = self.height(cur.left)
            rightH = self.height(cur.right)
            if leftH > rightH:
                count += 1
                count += 2**leftH-1
                cur = cur.right
            elif leftH == rightH:
                count += 1
                count += 2**rightH-1
                cur = cur.left
        return count

    def height(self, node):
        h = 0
        while node:
            node = node.right
            h += 1
        return h

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    # E = TreeNode(5)
    # F = TreeNode(6)
    A.left = B
    A.right = C
    B.left = D
    # B.right = E
    # C.left = F
    res = solu.countNodes3(A)
    print(res)