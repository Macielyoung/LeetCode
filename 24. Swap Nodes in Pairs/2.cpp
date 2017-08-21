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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL)
        {
            return head;
        }
        ListNode * dummy = head->next;
        head->next = dummy->next;
        dummy->next = head;
        //调用递归
        dummy->next->next = swapPairs(dummy->next->next);
        return dummy;
    }
};
