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
        if(n==0) return head;
        int length = 0;
        ListNode* dummy = head;
        //遍历链表，计算长度
        while(dummy != NULL)
        {
            dummy = dummy->next;
            length++;
        }
        if(length == n)
        {
            ListNode* res = head->next;
            delete head;
            return res;
        }
        else{
            //计算出删除节点的位置
            int loc = length - n - 1;
            dummy = head;
            while(loc--)
            {
                dummy = dummy->next;
            }
            ListNode* res = dummy->next;
            dummy->next = dummy->next->next;
            delete res;
            return head;
        }
    }
};
