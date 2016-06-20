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
    ListNode* partition(ListNode* head, int x) {
        ListNode* less = new ListNode(-1);
        ListNode* lesshead = less;
        ListNode* notless = new ListNode(-1);
        ListNode* notlesshead = notless;
        
        while (head != NULL)
        {
            if (head->val < x)
            {
                less->next = head;
                head = head->next;
                less = less->next;
                less->next = NULL;
            }
            else
            {
                notless->next = head;
                head = head->next;
                notless = notless->next;
                notless->next = NULL;
            }
        }
        less->next = notlesshead->next;
        return lesshead->next;
    }
};
