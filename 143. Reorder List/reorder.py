#-*- coding: UTF-8 -*-

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
            # 翻转右半部分链表
        fast = slow = head
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next

        fast = slow.next
        slow.next = None
        dummy = ListNode(0)
        while fast:
            node = dummy.next
            dummy.next = fast
            next_node = fast.next
            fast.next = node
            fast = next_node
        slow = head
        fast = dummy.next
        while slow:
            if fast != None:
                n1 = slow.next
                slow.next = fast
                n2 = fast.next
                fast.next = n1
                fast = n2
                slow = n1
            else:
                break

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    D = ListNode(4)
    E = ListNode(5)
    A.next = B
    # B.next = C
    # C.next = D
    # D.next = E
    solu.reorderList(A)

