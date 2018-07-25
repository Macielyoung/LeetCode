#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        num = 0
        pre = traverse = head
        while traverse:
            num += 1
            traverse = traverse.next
        mid = num // 2
        for i in range(mid-1):
            pre = pre.next
        cur = pre.next
        root = TreeNode(cur.val)
        pre.next = None
        cur = cur.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(cur)
        return root

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(-10)
    B = ListNode(-3)
    C = ListNode(0)
    D = ListNode(5)
    E = ListNode(9)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    root = solu.sortedListToBST(A)
    print root.val, root.left.val, root.right.val, root.left.left.val, root.right.left.val
