#-*- coding: UTF-8 -*-

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        cur = head
        # 第一步，在每个节点后面添加一个同样的节点
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next
        #第二步，把当前节点的随机指针指向节点的后一个节点赋给当前节点后一个节点的随机指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        #第三步，把复制的节点从原链表中剥离开
        new_head = head.next
        pold = head
        pnew = new_head
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return new_head

if __name__ == '__main__':
    solu = Solution()
    A = RandomListNode(1)
    B = RandomListNode(2)
    C = RandomListNode(3)
    D = RandomListNode(4)
    E = RandomListNode(5)
    F = RandomListNode(6)
    A.next = B
    A.random = D
    B.next = C
    C.next = D
    D.next = E
    E.next = F
    E.random = B
    newhead = solu.copyRandomList(A)
    print(newhead.label, newhead.random.label)
