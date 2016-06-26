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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (root == NULL) return {};
        queue <TreeNode*> qnode;
        queue <int> qlevel;
        stack <TreeNode*> snode;
        stack <int> slevel;
        qnode.push(root);
        qlevel.push(0);
        vector<vector<int>> res {{}};
        while (!qnode.empty())
        {
            root = qnode.front(); qnode.pop();
            int level = qlevel.front(); qlevel.pop();
            res[res.size()-1].push_back(root->val);
            if (level % 2 == 0)
            {
                if (root->left)
                {
                    snode.push(root->left);
                    slevel.push(level+1);
                }
                if (root->right)
                {
                    snode.push(root->right);
                    slevel.push(level+1);
                }
            }
            else
            {
                if (root->right)
                {
                    snode.push(root->right);
                    slevel.push(level+1);
                }
                if (root->left)
                {
                    snode.push(root->left);
                    slevel.push(level+1);
                }
            }
            if (qnode.empty() && !snode.empty())
            {
                while (!snode.empty())
                {
                    qnode.push(snode.top()); snode.pop();
                    qlevel.push(slevel.top()); slevel.pop();
                }
            }
            if (!qnode.empty() && level < qlevel.front())
                res.push_back({});
        }
        return res;
    }
};
