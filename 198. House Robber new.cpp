class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        vector <int> T (nums.size() + 1);
        T[1] = nums[0];
        for (int i = 2; i < nums.size() + 1; i++)
            T[i] = T[i - 1] > T[i - 2] + nums[i - 1] ? T[i - 1] : T[i - 2] + nums[i - 1];
        return T[nums.size()];
    }
};
