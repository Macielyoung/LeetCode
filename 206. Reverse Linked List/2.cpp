/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 * 递归实现
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL) return head;
        //调用递归
        ListNode *newhead = reverseList(head->next);
        //转向，头结点的下下个节点变为头结点
        head->next->next = head;
        //而头结点的下个节点为空，即为最后一个节点
        head->next = NULL;
        return newhead;
    }
};