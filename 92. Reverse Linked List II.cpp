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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) return head;
        ListNode* dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *p1 = dummy, *p2 = NULL, *rbegin = NULL, *rend = NULL, *nextnode = NULL;
        for (int i = 0; i < m-1; i++)
            p1 = p1->next;
        p2 = p1->next;
        for (int i = 0; i < n-m+1; i++)
        {
            rbegin = p2;
            p2 = p2->next;
            rbegin->next = nextnode;
            if (nextnode == NULL) rend = rbegin;
            nextnode = rbegin;
        }
        p1->next = rbegin;
        rend->next = p2;
        return dummy->next;
    }
};
