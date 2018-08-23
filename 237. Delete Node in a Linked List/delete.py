#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # pre = ListNode(-1)
        # pre.next = head
        node.val = node.next.val
        node.next = node.next.next

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(4)
    B = ListNode(5)
    C = ListNode(1)
    D = ListNode(9)
    A.next = B
    B.next = C
    C.next = D
    solu.deleteNode(B)
    print(A.next.val, A.next.next.val)