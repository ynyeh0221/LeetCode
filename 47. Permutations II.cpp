class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> path;
        vector<int> used (nums.size(), false);
        DFS(res, path, nums, used);
        return res;
    }
    void DFS(vector<vector<int>> &res, vector<int> &path, vector<int> &nums, vector<int> &used)
    {
        if (path.size() == nums.size())
        {
            res.push_back(path);
            return;
        }
        for (int i=0; i<nums.size(); i++)
        {
            if (!used[i])
            {
                if (i>0 && !used[i-1] && nums[i] == nums[i-1])
                    continue;
                used[i] = true;
                path.push_back(nums[i]);
                DFS(res, path, nums, used);
                path.pop_back();
                used[i] = false;
            }
        }
    }
};
