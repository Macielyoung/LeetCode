#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow = fast = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                slow = head
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    F = ListNode(6)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    F.next = B
    res = solu.detectCycle(A)
    print(res.val)
