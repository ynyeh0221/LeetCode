class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        else if (nums.size() == 1) return nums[0];
        else if (nums.size() == 2) return nums[0] > nums[1] ? nums[0] : nums[1];
        vector <int> T (nums.size());
        T[0] = nums[0]; T[1] = nums[1];
        for (int i = 2; i < nums.size(); i++)
        {
            int temp = T[i - 1];
            for (int j = 0; j < i -1; j++)
                temp = temp > T[j] + nums[i] ? temp : T[j] + nums[i];
            T[i] = T[i] > temp ? T[i] : temp;
        }
        return T[nums.size() - 1];
    }
};
