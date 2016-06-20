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
    bool isPalindrome(ListNode* head) {
        if (head == NULL) return true;
        ListNode* pfast = head;
        ListNode* pslow = head;
        while (pfast != NULL)
        {
            pfast = pfast->next;
            if (pfast != NULL)
            {
                pfast = pfast->next;
                pslow = pslow->next;
            }
        }
        ListNode* head2 = pslow;
        ListNode* nextnode = NULL;
        ListNode* dummy = new ListNode(-1);
        while (head2 != NULL)
        {
            ListNode* temp = head2;
            head2 = head2->next;
            temp->next = nextnode;
            dummy->next = temp;
            nextnode = dummy->next;
        }
        head2 = dummy->next;
        while (head != NULL && head2 != NULL)
        {
            if (head->val != head2->val) return false;
            head = head->next;
            head2 = head2->next;
        }
        return true;
    }
};
