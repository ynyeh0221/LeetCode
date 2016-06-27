class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector <int> res;
        for (int i = nums.size()-1; i >=0; i--)
        {
            vector <int> temp {nums[i]};
            int pre = nums[i];
            for (int j = i-1; j >= 0; j--)
            {
                if (pre % nums[j] == 0)
                {
                    temp.push_back(nums[j]);
                    pre = nums[j];
                }
            }
            if (res.size() < temp.size()) res = temp;
        }
        return res;
    }
};
