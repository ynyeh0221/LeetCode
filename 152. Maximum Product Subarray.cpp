class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector <vector <int>> T (nums.size() + 1, vector<int>(2, 0));
        T[1][0] = nums[0];
        T[1][1] = nums[0];
        int res = nums[0];
        for (int i = 2; i <= nums.size(); i++)
        {
            int temp = T[i-1][0] * nums[i-1] > T[i-1][1] * nums[i-1] ? T[i-1][0] * nums[i-1] : T[i-1][1] * nums[i-1];
            T[i][0] = temp > nums[i-1] ? temp : nums[i-1];
            temp = T[i-1][0] * nums[i-1] < T[i-1][1] * nums[i-1] ? T[i-1][0] * nums[i-1] : T[i-1][1] * nums[i-1];
            T[i][1] = temp < nums[i-1] ? temp : nums[i-1];
            res = res > T[i][0] ? res : T[i][0];
        }
        return res;
    }
};
