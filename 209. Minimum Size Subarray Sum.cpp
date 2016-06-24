class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int l = 0, r = 0;
        int res = nums.size() + 1;
        while (r < nums.size())
        {
            int sum = 0;
            for (int i = l; i <= r; i++)
                sum += nums[i];
            if (sum < s) r++;
            else
            {
                res = res < r+1-l ? res : r+1-l;
                l++;
            }
        }
        return res == nums.size() + 1 ? 0 : res;
    }
};
