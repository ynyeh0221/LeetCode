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
    ListNode* oddEvenList(ListNode* head) {
        ListNode* odd = new ListNode(-1);
        ListNode* even = new ListNode(-1);
        ListNode* oddhead = odd;
        ListNode* evenhead = even;
        while (head != NULL)
        {
            odd->next = head;
            head = head->next;
            odd = odd->next;
            odd->next = NULL;
            if (head != NULL)
            {
                even->next = head;
                head = head->next;
                even = even->next;
                even->next = NULL;
            }
        }
        odd->next = evenhead->next;
        return oddhead->next;
    }
};
