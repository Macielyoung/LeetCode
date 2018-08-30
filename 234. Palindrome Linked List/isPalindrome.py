#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        cur = head
        values = []
        while cur:
            values.append(cur.val)
            cur = cur.next
        if(values == values[::-1]):
            return True
        else:
            return False

    # 翻转后半list
    def isPalindrome2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            nextN = slow.next
            slow.next = node
            node = slow
            slow = nextN
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(3)
    E = ListNode(2)
    F = ListNode(1)
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    # E.next = F
    res = solu.isPalindrome2(A)
    print(res)