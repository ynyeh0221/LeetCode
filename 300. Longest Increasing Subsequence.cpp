class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        vector <int> T (nums.size(), 1);
        int res = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j] && T[j] + 1 > T[i])
                    T[i] = T[j] + 1;
            }
            res = T[i] > res ? T[i] : res;
        }
        return res;
    }
};
