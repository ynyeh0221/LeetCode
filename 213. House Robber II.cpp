class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        vector <int> T0 (n+1);
        vector <int> T1 (n+1);
        T0[1] = nums[0]; T1[2] = nums[1];
        for (int i = 2; i < n; i++)
            T0[i] = T0[i-2] + nums[i-1] > T0[i-1] ? T0[i-2] + nums[i-1] : T0[i-1];
        for (int i = 3; i <= n; i++)
            T1[i] = T1[i-2] + nums[i-1] > T1[i-1] ? T1[i-2] + nums[i-1] : T1[i-1];
        return T0[n-1] > T1[n] ? T0[n-1] : T1[n];
    }
};
