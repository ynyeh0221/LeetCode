/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        DFS(root);
    }
    
    void DFS(TreeLinkNode *root)
    {
        if (root == NULL || (root->left == NULL && root->right == NULL)) return;
        root->left->next = root->right;
        if (root->next)
            root->right->next = root->next->left;
        else
            root->right->next = NULL;
        DFS(root->left);
        DFS(root->right);
    }
};
