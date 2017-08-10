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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(!l1) return l2;
        if(!l2) return l1;
        
        ListNode* start;
        ListNode* cur;
        if(l1->val < l2->val)
        {
            start = cur = l1;
            l1 = l1->next;
        }
        else{
            start = cur = l2;
            l2 = l2->next;
        }
        while(l1 != NULL && l2 != NULL)
        {
            if(l1->val < l2->val)
            {
                cur->next = l1;
                cur = l1;
                l1 = l1->next;
            }
            else{
                cur->next = l2;
                cur = l2;
                l2 = l2->next;
            }
        }
        if(l1 != NULL)
        {
            cur->next = l1;
        }
        else{
            cur->next = l2;
        }
        return start;
    }
};