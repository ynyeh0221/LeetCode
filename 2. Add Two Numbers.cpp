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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *dummy = new ListNode(-1);
        ListNode *p = dummy;
        
        while (l1 && l2)
        {
            ListNode *temp = l1->val + l2->val + carry >= 10 ? new ListNode(l1->val + l2->val + carry - 10) : new ListNode(l1->val + l2->val +carry);
            carry = l1->val + l2->val + carry >= 10 ? 1 : 0;
            p->next = temp;
            p = p -> next;
            l1 = l1 -> next;
            l2 = l2 -> next;
        }
        while (l1)
        {
            ListNode *temp = l1->val + carry >= 10 ? new ListNode(l1->val + carry - 10) : new ListNode(l1->val + carry);
            carry = l1->val + carry >= 10 ? 1 : 0;
            p->next = temp;
            p = p -> next;
            l1 = l1 -> next;
        }
        while (l2)
        {
            ListNode *temp = l2->val + carry >= 10 ? new ListNode(l2->val + carry - 10) : new ListNode(l2->val +carry);
            carry = l2->val + carry >= 10 ? 1 : 0;
            p->next = temp;
            p = p -> next;
            l2 = l2 -> next;
        }
        if (carry)
        {
            ListNode *temp = new ListNode(1);
            p->next = temp;
        }
        return dummy->next;
    }
};
