#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while not head or not head.next:
            return False
        slow = fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if (slow == fast):
                return True
        return False

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    # B = ListNode(2)
    # C = ListNode(3)
    # D = ListNode(4)
    # A.next = B
    # B.next = C
    # C.next = D
    # D.next = A
    res = solu.hasCycle(A)
    print(res)