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
    int countNodes(TreeNode* root) {
        if (root == NULL) return 0;
        int l = lheight(root) + 1;
        int r = rheight(root) + 1;
        if (l == r) return pow(2, l) -1;
        else return countNodes(root->left) + countNodes(root->right) + 1;
    }
    int lheight(TreeNode* root)
    {
        int count = 0;
        while (root->left != NULL)
        {
            root = root->left;
            count ++;
        }
        return count;
    }
    int rheight(TreeNode* root)
    {
        int count = 0;
        while (root->right != NULL)
        {
            root = root->right;
            count ++;
        }
        return count;
    }
};
