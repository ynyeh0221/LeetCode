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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (root == NULL)
            return res;
        queue<TreeNode*> nodes;
        queue<int> level;
        res.push_back({});
        nodes.push(root);
        level.push(0);
        while (nodes.size() > 0 and level.size() > 0)
        {
            TreeNode* p = nodes.front();
            nodes.pop();
            int l = level.front();
            level.pop();
            res[res.size()-1].push_back(p->val);
            if (p->left != NULL)
            {
                nodes.push(p->left);
                level.push(l + 1);
            }
            if (p->right != NULL)
            {
                nodes.push(p->right);
                level.push(l + 1);
            }
            if (nodes.size() > 0 && l != level.front())
                res.push_back({});
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
