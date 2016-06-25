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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (inorder.size() == 0) return NULL;
        vector<int>::iterator it;
        int ind = find (inorder.begin(), inorder.end(), preorder[0]) - inorder.begin();
        preorder.erase(preorder.begin());
        TreeNode* root = new TreeNode(inorder[ind]);
        vector <int> left(inorder.begin(), inorder.begin() + ind);
        vector <int> right(inorder.begin() + ind + 1, inorder.end());
        root->left = buildTree(preorder, left);
        root->right = buildTree(preorder, right);
        return root;
    }
};
