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
    ListNode* reverseList(ListNode* head) {
        ListNode * dummy = new ListNode(-1);
        dummy->next = head;
        ListNode * p1 = head;
        ListNode * p2 = head;
        ListNode * nextnode = NULL;
        
        while (p1 != NULL)
        {
            p2 = p1->next;
            p1->next = nextnode;
            dummy->next = p1;
            nextnode = p1;
            p1 = p2;
        }
        return dummy->next;
    }
};
