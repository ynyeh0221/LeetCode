class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector <int> res (nums.size(), 1);
        int temp = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            temp *= nums[i-1];
            res[i] *= temp;
        }
        temp = 1;
        for (int i = nums.size()-2; i >= 0; i--)
        {
            temp *= nums[i+1];
            res[i] *= temp;
        }
        return res;
    }
};
