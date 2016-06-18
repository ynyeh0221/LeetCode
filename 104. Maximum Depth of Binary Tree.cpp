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
    int maxDepth(TreeNode* root) {
        return height(root, 0);
    }
    
    int height(TreeNode* root, int h)
    {
        if (root == NULL) return h;
        int l = height(root->left, h), r = height(root->right, h);
        return l > r ? l + 1 : r + 1;
    }
};
