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
private:
    bool res = true;
public:
    bool isSymmetric(TreeNode* root) {
        symm(root, root);
        return res;
    }
    
    void symm(TreeNode* p1, TreeNode* p2)
    {
        if (p1 == NULL && p2 == NULL)
            return;
        else if (p1 != NULL && p2 == NULL)
        {
            res = false;
            return;
        }
        else if (p1 == NULL && p2 != NULL)
        {
            res = false;
            return;
        }
        if (p1->val != p2->val)
        {
            res = false;
            return;
        }
        symm(p1->left, p2->right);
        symm(p1->right, p2->left);
    }
};
