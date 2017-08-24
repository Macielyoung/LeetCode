/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 非递归实现
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL) return NULL;
        ListNode *pre = head;
        ListNode *cur = head->next;
        while(cur!=NULL)
        {
            //记录下一个节点
            pre->next = cur->next;
            //用于转向，当前节点的下个节点是头结点，而原来的头结点则变为当前节点
            cur->next = head;
            head = cur;
            //记录的当前节点变为开始记录的下一个节点
            cur = pre->next;
        }
        return head;
    }
};