#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    #使用库函数排序
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return sorted(nums)

    def merge(self, n1, n2):
        cur = tail = ListNode(None)
        while n1 and n2:
            if n1.val < n2.val:
                tail.next, tail, n1 = n1, n1, n1.next
            else:
                tail.next, tail, n2 = n2, n2, n2.next
        tail.next = n1 or n2
        return cur.next

    def sortList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next:
            return head
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        return self.merge(*map(self.sortList, (head, slow)))

if __name__ == '__main__':
    solu = Solution()
    A = ListNode(4)
    B = ListNode(2)
    C = ListNode(1)
    D = ListNode(3)
    A.next = B
    B.next = C
    C.next = D
    res = solu.sortList(A)
    res2 = solu.sortList2(A)
    print(res, res2.val)
