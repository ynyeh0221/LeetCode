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
    int kthSmallest(TreeNode* root, int k) {
        int res = 0;
        inorder(root, k, res);
        return res;
    }
    
    void inorder(TreeNode* root, int &k, int &res)
    {
        if (root == NULL)
            return;
        inorder(root->left, k, res);
        k--;
        if (k == 0)
        {
            res = root->val;
            return;
        }
        inorder(root->right, k, res);
    }
};
