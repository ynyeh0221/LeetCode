class Solution {
public:
    int missingNumber(vector<int>& nums) {
        vector <int> allnums;
        for (int i = 0; i<nums.size()+1; i++)
            allnums.push_back(i);
        int res = allnums[0];
        for (int i = 1; i<allnums.size(); i++)
            res ^= allnums[i];
        for (int i = 0; i<nums.size(); i++)
            res ^= nums[i];
        return res;
    }
};
