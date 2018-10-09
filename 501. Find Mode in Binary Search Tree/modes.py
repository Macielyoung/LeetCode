#-*- coding: UTF-8 -*-

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 基本方法，完全没有考虑二叉搜索树的特性
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic = {}
        nodes = [(root, 0)]
        while nodes:
            cur, h = nodes.pop()
            if cur.val not in dic:
                dic[cur.val] = 1
            else:
                dic[cur.val] += 1
            if cur.left:
                nodes.append((cur.left, h+1))
            if cur.right:
                nodes.append((cur.right, h+1))
        max_freq = 0
        for v in dic.values():
            if v > max_freq:
                max_freq = v
        res = [k for k, v in dic.items() if v==max_freq]
        return res

    def findMode2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        pre, cur, stack, cur_count, max_count, modes = None, root, [], 0, 0, []
        # 中序遍历二叉树
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not pre or cur.val == pre.val:
                cur_count += 1
            else:
                if cur_count > max_count:
                    max_count = cur_count
                    modes = [pre.val]
                elif cur_count == max_count:
                    modes.append(pre.val)
                cur_count = 1
            pre = cur    # 谨记前一个节点的值
            cur = cur.right
        if cur_count > max_count:  # 如果最后的数出现次数大于modes中数的次数，则保留最后这个数
            return [pre.val]
        elif cur_count == max_count:
            modes.append(pre.val)
        return modes

    def inorder(self, root):
        if not root:
            return []
        cur, stack, res = root, [], []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

if __name__ == '__main__':
    solu = Solution()
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(2)
    A.right = B
    B.left = C
    res = solu.findMode2(A)
    print(res)

    # A = TreeNode(4)
    # B = TreeNode(2)
    # C = TreeNode(6)
    # D = TreeNode(1)
    # E = TreeNode(3)
    # F = TreeNode(5)
    # G = TreeNode(7)
    # A.left = B
    # A.right = C
    # B.left = D
    # B.right = E
    # C.left = F
    # C.right = G
    # res = solu.inorder(A)