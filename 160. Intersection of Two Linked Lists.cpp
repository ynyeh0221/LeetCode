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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *pA = headA, *pB = headB;
        int lengthA = 0, lengthB = 0;
        while (pA != NULL)
        {
            lengthA++;
            pA = pA->next;
        }
        while (pB != NULL)
        {
            lengthB++;
            pB = pB->next;
        }
        for (int i = 0; i < abs(lengthA - lengthB); i++)
            lengthA > lengthB ? headA = headA->next : headB = headB->next;
        while (headA != NULL && headB != NULL)
        {
            if (headA == headB) return headA;
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
    }
};
