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
private:
    int minheight = INT_MAX;
public:
    int minDepth(TreeNode* root) {
        if (root == NULL) return 0;
        DFS(root, 0);
        return minheight;
    }
    
    void DFS(TreeNode* root, int height)
    {
        if (root == NULL) return;
        else if (root->left == NULL && root->right == NULL)
        {
            if (height + 1 < minheight) minheight = height + 1;
            return;
        }
        DFS(root->left, height + 1);
        DFS(root->right, height + 1);
    }
};
