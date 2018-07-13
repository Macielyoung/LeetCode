#-*- coding: UTF-8 -*-

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 遍历list，使用dict记录各个值的出现次数
        cursor = head
        dict = {}
        if not head:
            return None
        while cursor:
            dict[cursor.val] = dict.get(cursor.val, -1) + 1
            cursor = cursor.next
        head = self.delete(head, dict)
        return head

    def delete(self, node, dict):
        if not node: return None
        if dict[node.val]: return self.delete(node.next, dict)
        if not dict[node.val]:
            node.next = self.delete(node.next, dict)
            return node


if __name__ == '__main__':
    solu = Solution()
    head = ListNode(0)
    A = ListNode(1)
    B = ListNode(1)
    C = ListNode(1)
    D = ListNode(2)
    E = ListNode(3)
    head.next = A
    A.next = B
    B.next = C
    C.next = D
    D.next = E
    new_head = solu.deleteDuplicates(head)
    print(new_head.val)
    print(new_head.next.val)
    print(new_head.next.next.val)