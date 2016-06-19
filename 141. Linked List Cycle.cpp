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
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        ListNode *pslow = head;
        ListNode *pfast = head->next;
        while (pfast != NULL)
        {
            pslow = pslow->next;
            pfast = pfast->next;
            if (pfast != NULL)
                pfast = pfast->next;
            if (pslow == pfast)
                return true;
        }
        return false;
    }
};
