#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = ListNode(None)
        pre.next = head
        cur = head
        insertion = prev = ListNode(None)
        while cur and cur.next:
            if(cur.val <= cur.next.val):
                cur = cur.next
            else:
                insertion = cur.next
                cur.next = insertion.next
                prev = pre
                while(prev.next.val <= insertion.val):
                    prev = prev.next
                insertion.next = prev.next
                prev.next = insertion
        return pre.next

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(4)
    B = ListNode(2)
    C = ListNode(1)
    D = ListNode(3)
    A.next = B
    B.next = C
    C.next = D
    res = solu.insertionSortList(A)
    print(res.val, res.next.val)