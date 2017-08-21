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
        ListNode *dummy = new ListNode(0);  
        dummy->next = head;  
        ListNode *preNode = dummy, *curNode = head;   
        while (curNode != NULL && curNode->next != NULL) {  
            //交换相邻的两个节点  
            preNode->next = curNode->next;  
            curNode->next = preNode->next->next;  
            preNode->next->next = curNode;  
              
            //向后跳两个节点
            preNode = curNode;  
            curNode = curNode->next;  
        }  
        head = dummy->next;  
        delete dummy;  
        return head;  
    }
};
