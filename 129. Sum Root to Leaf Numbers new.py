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
    int res = 0;
public:
    int sumNumbers(TreeNode* root) {
        preorder(0, root);
        return res;
    }
    
    void preorder(int pathsum, TreeNode* root)
    {
        if (root == NULL) return;
        if (root->left == NULL && root->right == NULL)
            res += 10 * pathsum + root->val;
        preorder(10 * pathsum + root->val, root->left);
        preorder(10 * pathsum + root->val, root->right);
    }
};
