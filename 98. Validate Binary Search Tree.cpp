/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <climits>
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (root == NULL) return true;
        return check(root, LONG_MIN, LONG_MAX);
    }
    
    bool check(TreeNode* root, long long int lower, long long int upper)
    {
        return root->val > lower && root->val < upper && ((root->left ? check(root->left, lower, root->val) : true) && (root->right ? check(root->right, root->val, upper) : true));
    }
};
