/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        if(head == NULL) return NULL;
        //用于记录删除节点的前一个节点
        ListNode* pre = NULL;
        ListNode* p = head;
        ListNode* q = head;
        //先走n-1步
        for(int i=0;i<n-1;i++)
        {
            q = q->next;
        }
        while(q->next)
        {
            pre = p;
            p = p->next;
            q = q->next;
        }
        //如果n大于等于链表长度
        if(pre == NULL)
        {
            head = p->next;
            delete p;
        }
        else{
            pre->next = p->next;
            delete p;
        }
        return head;
    }
};