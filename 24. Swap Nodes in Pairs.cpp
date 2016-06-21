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
        if (head == NULL or head->next == NULL) return head;
        ListNode* dummy = new ListNode(-1);
        ListNode* p = dummy, *p1 = head, *p2 = p1->next;
        while (p1 != NULL && p2 != NULL)
        {
            p->next = p2;
            p1->next = p2->next;
            p2->next = p1;
            p = p1;
            p1 = p1->next;
            if (p1 != NULL) p2 = p1->next;
        }
        return dummy->next;
    }
};
