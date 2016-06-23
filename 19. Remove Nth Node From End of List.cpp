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
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode* p1 = dummy;
        ListNode* p2 = head;
        while (n > 0)
        {
            p2 = p2->next;
            n--;
        }
        while (p2 != NULL)
        {
            p1 = p1->next;
            p2 = p2->next;
        }
        if (p1->next == NULL) p1->next = NULL;
        else p1->next = p1->next->next;
        return dummy->next;
    }
};
