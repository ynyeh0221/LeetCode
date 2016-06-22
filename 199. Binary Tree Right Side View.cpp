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
public:
    vector<int> rightSideView(TreeNode* root) {
        if (root == NULL) return {};
        queue <TreeNode*> nodes;
        queue <int> levels;
        nodes.push(root);
        levels.push(0);
        int level = 0;
        vector <int> res;
        while (!nodes.empty() && !levels.empty())
        {
            root = nodes.front(); nodes.pop();
            level = levels.front(); levels.pop();
            if (res.size() == level)
                res.push_back(root->val);
            if (root->right)
            {
                nodes.push(root->right);
                levels.push(level + 1);
            }
            if (root->left)
            {
                nodes.push(root->left);
                levels.push(level + 1);
            }
        }
        return res;
    }
};
