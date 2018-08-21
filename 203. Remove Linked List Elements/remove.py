#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        pre, cur = ListNode(-1), head
        new_head = pre
        pre.next = head
        while(cur.next):
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        if(cur.val == val):
            pre.next = None
        return new_head.next

    # 使用一个变量
    def removeElements2(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head

        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return dummy_head.next

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(6)
    D = ListNode(3)
    E = ListNode(4)
    F = ListNode(5)
    G = ListNode(6)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G
    head = solu.removeElements2(A, 1)
    print(head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val, head.next.next.next.next.next)