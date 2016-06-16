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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* p = head;
        ListNode* pre = dummy;
        
        while (p != NULL)
        {
            if (p->val == val)
            {
                pre->next = p->next;
                delete p;
                p = pre->next;
            }
            else
            {
                p = p->next;
                pre = pre->next;
            }
        }
        return dummy->next;
    }
};
