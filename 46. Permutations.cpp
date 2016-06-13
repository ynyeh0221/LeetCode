class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> path;
        vector<vector<int>> res;
        DFS(res, path, nums);
        return res;
    }
    
    void DFS(vector<vector<int>>& res, vector<int>& path, vector<int>& nums)
    {
        if (path.size() == nums.size())
        {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (find(path.begin(), path.end(), nums[i]) == path.end())
            {
                path.push_back(nums[i]);
                DFS(res, path, nums);
                path.pop_back();
            }
        }
    }
};
