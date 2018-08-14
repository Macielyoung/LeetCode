#-*- coding: UTF-8 -*-
from collections import deque

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return None
        dict = {}
        nodes = [(root, 0)]
        while nodes:
            cur, height = nodes.pop()
            if height not in dict.keys():
                dict[height] = [cur]
            else:
                dict[height].append(cur)
            if cur.right:
                nodes.append((cur.right, height+1))
            if cur.left:
                nodes.append((cur.left, height+1))
        for nkey in dict.keys():
            if len(dict[nkey]) > 1:
                for i in range(len(dict[nkey])-1):
                    dict[nkey][i].next = dict[nkey][i+1]
        return dict

    def connect2(self, root):
        if root == None:
            return
        queue, level, cur = root, None, None
        while queue:
            if queue.left:
                if not level:
                    level = cur = queue.left
                else:
                    cur.next = queue.left
                    cur = cur.next
            if queue.right:
                if not level:
                    level = cur = queue.right
                else:
                    cur.next = queue.right
                    cur = cur.next
            queue = queue.next
            if not queue and level:
                queue, level, curr = level, None, None

    def connect3(self, root):
        if root == None:
            return
        queue, level = deque([root]), deque()
        while queue:
            node = queue.popleft()
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            node.next = queue[0] if queue else None
            if not queue and level:
                queue, level = level, queue


if __name__ == '__main__':
    solu = Solution()
    A = TreeLinkNode(0)
    B = TreeLinkNode(1)
    C = TreeLinkNode(2)
    D = TreeLinkNode(3)
    E = TreeLinkNode(4)
    # F = TreeLinkNode(5)
    G = TreeLinkNode(6)
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    # C.left = F
    C.right = G
    # dic = solu.connect(A)
    solu.connect3(A)
    print(A.left.right.next.val)