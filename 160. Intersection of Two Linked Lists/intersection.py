#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == headB:
            return headA
        first, second = headA, headB
        num1, num2 = 0, 0
        while first:
            num1 += 1
            first = first.next
        while second:
            num2 += 1
            second = second.next
        if(num2 > num1):
            fast = headB
            slow = headA
        else:
            fast = headA
            slow = headB
        for i in range(abs(num1-num2)):
            fast = fast.next
        while(fast != slow):
            fast = fast.next
            slow = slow.next
        return fast

if __name__ == '__main__':
    solu = Solution()
    A1 = ListNode(1)
    A2 = ListNode(2)
    A3 = ListNode(3)
    A4 = ListNode(4)
    B2 = ListNode(5)
    B1 = ListNode(4)
    A1.next = A2
    A2.next = A3
    A3.next = A4
    B1.next = B2
    B2.next = A3
    res = solu.getIntersectionNode(A1, B1)
    print(res.val)
