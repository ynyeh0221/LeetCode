/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class BSTIterator {
private:
    vector <int> nums;
    stack <TreeNode*> s;
public:
    BSTIterator(TreeNode *root) {
        if (root == NULL) return;
        s.push(root);
        while (!s.empty())
        {
            while (root != NULL)
            {
                s.push(root);
                root = root->left;
            }
            root = s.top(); s.pop();
            nums.push_back(root->val);
            root = root->right;
        }
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return nums.size() > 1 ? true : false;
    }

    /** @return the next smallest number */
    int next() {
        int temp = nums[0];
        nums.erase(nums.begin());
        return temp;
    }
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
