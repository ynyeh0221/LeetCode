class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector <int> T (nums.size() + 1, 0);
        T[1] = nums[0]; //-INT_MAX => overflow
        int res = nums[0];
        for (int i = 2; i <= nums.size(); i++)
        {
            T[i] = T[i-1] + nums[i-1] > nums[i-1] ? T[i-1] + nums[i-1] : nums[i-1];
            res = T[i] > res ? T[i] : res;
        }
        return res;
    }
};
