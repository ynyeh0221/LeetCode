/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return build(head, NULL);
    }
    TreeNode* build(ListNode* left, ListNode* right)
    {
        if (left == right) return NULL;
        ListNode* mid = findmid(left, right);
        TreeNode* root = new TreeNode(mid->val);
        root->left = build(left, mid);
        root->right = build(mid->next, right);
        return root;
    }
    ListNode* findmid(ListNode* left, ListNode* right)
    {
        ListNode* p1 = left;
        ListNode* p2 = left;
        while (p2 != right)
        {
            p2 = p2->next;
            if (p2 != right)
            {
                p2 = p2->next;
                p1 = p1->next;
            }
        }
        return p1;
    }
};
