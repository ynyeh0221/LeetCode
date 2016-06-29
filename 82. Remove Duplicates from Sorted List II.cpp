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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* p1 = dummy, *p2 = head;
        while (p2 != NULL && p2->next != NULL)
        {
            if (p2->val == p2->next->val)
            {
                while (p2 != NULL && p2->next != NULL && p2->val == p2->next->val)
                    p2 = p2->next;
                p2 = p2->next;
                p1->next = p2;
            }
            else
            {
                p1 = p1->next;
                p2 = p2->next;
            }
        }
        return dummy->next;
    }
};
