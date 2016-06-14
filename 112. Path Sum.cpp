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
    bool hasPathSum(TreeNode* root, int sum) {
        if (root == NULL) return false;
        bool res = false;
        DFS(root, sum, res);
        return res;
    }
    
    void DFS(TreeNode* root, int sum, bool &res)
    {
        if (root == NULL)
            return;
        if (root->left == NULL && root->right == NULL)
        {
            if (sum == root->val)
                res = true;
        }
        DFS(root->left, sum - root->val, res);
        DFS(root->right, sum - root->val, res);
    }
};
