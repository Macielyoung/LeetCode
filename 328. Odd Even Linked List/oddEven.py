#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next==None or head.next.next==None:
            return head
        odd, even = head, head.next
        evenHead = even
        while even != None and even.next != None:
            # 奇数位指向下一个奇数位
            odd.next = even.next
            odd = odd.next
            # 偶数位指向下一个偶数位
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    F = ListNode(6)
    G = ListNode(7)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = G
    res = solu.oddEvenList(A)
    print(res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next.val)