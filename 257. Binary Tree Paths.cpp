/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
#include <sstream>
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector <string> res;
        preorder({}, root, res);
        return res;
    }
    
    void preorder(vector <int> path, TreeNode* root, vector <string> &res)
    {
        if (root == NULL)
            return;
        if (root->left == NULL && root->right == NULL)
        {
            path.push_back(root->val);
            stringstream ss;
            for(size_t i = 0; i < path.size(); ++i)
            {
                if(i != 0)
                    ss << "->";
                ss << path[i];
            }
            string s = ss.str();
            res.push_back(s);
            path.pop_back();
        }
        path.push_back(root->val);
        preorder(path, root->left, res);
        preorder(path, root->right, res);
        path.pop_back();
    }
};
