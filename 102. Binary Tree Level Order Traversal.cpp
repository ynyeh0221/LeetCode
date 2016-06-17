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
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (root == NULL) return {};
        queue <TreeNode*> q;
        queue <int> level;
        q.push(root);
        level.push(0);
        vector <vector<int>> res;
        res.push_back({});
        
        while (!q.empty())
        {
            TreeNode* curr_node = q.front();
            q.pop();
            int curr_level = level.front();
            level.pop();
            res[res.size() - 1].push_back(curr_node->val);
            if (curr_node->left != NULL)
            {
                q.push(curr_node->left);
                level.push(curr_level+1);
            }
            if (curr_node->right != NULL)
            {
                q.push(curr_node->right);
                level.push(curr_level+1);
            }
            if (q.size() > 0 && level.front() > curr_level)
                res.push_back({});
        }
        return res;
    }
};
