#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head == None or m == n:
            return head
        cur = head
        count = 1
        before_tail = ListNode(-1)
        # 计算前半段的尾结点
        while(count != m):
            before_tail = cur
            cur = cur.next
            count += 1

        reversed_head = cur
        prev = cur
        cur = cur.next
        count += 1
        reverse_tail_loc = n+1
        # 反转链表
        while(count != reverse_tail_loc):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count += 1

        reversed_head.next = cur
        if(m!=1):
            before_tail.next = prev
        else:
            return prev
        return head

if __name__ == '__main__':
    solu = Solution()
    head = ListNode(1)
    A = ListNode(2)
    B = ListNode(3)
    C = ListNode(4)
    D = ListNode(5)
    head.next = A
    A.next = B
    B.next = C
    C.next = D
    new_head = solu.reverseBetween(head, 2, 4)
    # print(head.val)
    print(new_head.val)
    print(new_head.next.val)
    print(new_head.next.next.val)
    print(new_head.next.next.next.val)