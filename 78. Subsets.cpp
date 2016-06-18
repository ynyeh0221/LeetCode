class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        res.push_back({});
        for (int k = 1; k <= nums.size(); k++)
            combination(nums, {}, 0, k);
        return res;
    }
    
    void combination(vector<int>& nums, vector<int> path, int start, int k)
    {
        if (path.size() == k)
            res.push_back(path);
        for (int i = start; i < nums.size(); i++)
        {
            path.push_back(nums[i]);
            combination(nums, path, i + 1, k);
            path.pop_back();
        }
    }
};
