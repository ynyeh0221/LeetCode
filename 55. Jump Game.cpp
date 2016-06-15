class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector <int> T (nums.size());
        T[0] = nums[0];
        if (nums.size() > 1 && T[0] < 1)
            return false;
        for (int i = 0; i < nums.size(); i++)
        {
            T[i] = T[i-1] > nums[i] + i ? T[i-1] : nums[i] + i;
            if (nums.size() > i + 1 && T[i] < i + 1)
                return false;
        }
        return true;
    }
};
