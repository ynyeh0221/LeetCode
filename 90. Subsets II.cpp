class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        res.push_back({});
        sort(nums.begin(), nums.end());
        for (int k = 1; k <= nums.size(); k++)
            combination(nums, {}, 0, k);
        return res;
    }
    
    void combination(vector<int>& nums, vector<int> path, int start, int k)
    {
        if (path.size() == k)
            res.push_back(path);
        int i = start;
        while (i < nums.size())
        {
            path.push_back(nums[i]);
            combination(nums, path, i + 1, k);
            path.pop_back();
            i++;
            while (i < nums.size() && nums[i] == nums[i-1])
                i++;
        }
    }
};
