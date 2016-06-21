class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector <int> res;
        vector <int> notexist {-1,-1};
        if (nums[0] == target) res.push_back(0);
        for (int i = 1; i < nums.size(); i++)
        {
            if (res.size() == 2) break;
            if (nums[i-1] != target && nums[i] == target) res.push_back(i);
            else if (nums[i-1] == target && nums[i] != target) res.push_back(i-1);
        }
        if (res.size() == 1) res.push_back(nums.size() - 1);
        return res.size() > 0 ? res : notexist;
    }
};
