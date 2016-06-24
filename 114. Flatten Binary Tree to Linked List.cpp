/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <queue>
class Solution {
private:
    queue <TreeNode*> q; 
public:
    void flatten(TreeNode* root) {
        if (!(root == NULL || (root->left == NULL && root->right == NULL)))
        {
            TreeNode* p = root;
            preorder(p);
            while (!q.empty())
            {
                TreeNode* curr = q.front();
                q.pop();
                p->right = curr;
                p->left = NULL;
                p = p->right;
            }
        }
    }
    void preorder(TreeNode* p)
    {
        if (p == NULL) return;
        q.push(p);
        preorder(p->left);
        preorder(p->right);
    }
};
