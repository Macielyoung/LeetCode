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
    ListNode* reverseKGroup(ListNode* head, int k) {
        //如果链表为空，或者只有一个元素，亦或者k的值小于2，则返回链表本身
        if(head==NULL || head->next==NULL || k<2)
        {
            return head;
        }
        ListNode *dummy = head;
        //遍历k个节点
        for(int i=0;i<k;i++)
        {
            if(dummy)
            {
                dummy = dummy->next;
            }
            //不足k个节点，则直接返回原来的顺序
            else{
                return head;
            }
        }
        ListNode *pre = NULL, *cur = head, *next = NULL;
        //反转前k个节点，再递归处理后面的节点
        while(cur!=dummy)
        {
            next = cur->next;
            if(pre)
            {
                cur->next = pre;
            }
            else{
                cur->next = reverseKGroup(dummy, k);
            }
            pre = cur;
            cur = next;
        }
        return pre;
    }
};