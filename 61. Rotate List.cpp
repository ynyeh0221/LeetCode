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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == NULL) return head;
        ListNode* p = head;
        int length = 0;
        while (p != NULL && p->next != NULL)
        {
            length ++;
            p = p->next;
        }
        length ++;
        p->next = head;
        k %= length;
        for (int i = 0; i < length - k; i++)
            p = p->next;
        ListNode* newhead = p->next;
        p->next = NULL;
        return newhead;
    }
};
