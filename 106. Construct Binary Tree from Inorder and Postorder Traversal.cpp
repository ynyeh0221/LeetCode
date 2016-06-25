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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() == 0) return NULL;
        int ind = find(inorder.begin(), inorder.end(), postorder[postorder.size()-1]) - inorder.begin();
        postorder.erase(postorder.end()-1);
        TreeNode* root = new TreeNode(inorder[ind]);
        vector <int> left(inorder.begin(), inorder.begin()+ind);
        vector <int> right(inorder.begin()+ind+1, inorder.end());
        root->right = buildTree(right, postorder);
        root->left = buildTree(left, postorder);
        return root;
    }
};
