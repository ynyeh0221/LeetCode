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
    bool isBalanced(TreeNode* root) {
        if (root == NULL || (root->left == NULL && root->right == NULL)) return true;
        if (abs(height(root->left, 0) - height(root->right, 0)) > 1) return false;
        else if (!isBalanced(root->left) || !isBalanced(root->right)) return false;
        return true;
    }
    
    int height(TreeNode* root, int h)
    {
        if (root == NULL) return h;
        int l = height(root->left, h), r = height(root->right, h);
        return l > r ? l + 1 : r + 1;
    }
};
