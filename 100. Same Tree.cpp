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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        bool res = true;
        preorder(p, q, res);
        return res;
    }
    
    void preorder(TreeNode* p, TreeNode* q, bool &res)
    {
        if (p == NULL && q == NULL)
            return;
        else if (p != NULL && q == NULL)
        {
            res = false;
            return;
        }
        else if (p == NULL && q != NULL)
        {
            res = false;
            return;
        }
        if (p->val != q->val)
            res = false;
        preorder(p->left, q->left, res);
        preorder(p->right, q->right, res);
    }
};
