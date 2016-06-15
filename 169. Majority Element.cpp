class Solution {
public:
    int majorityElement(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        vector<int> sub_l(nums.begin(), nums.begin() + nums.size()/2);
        vector<int> sub_r(nums.begin() + nums.size()/2, nums.begin() + nums.size());
        int majority_l = majorityElement(sub_l);
        int majority_r = majorityElement(sub_r);
        int temp_l = 0, temp_r = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == majority_l)
            {
                temp_l ++;
                if (temp_l > nums.size()/2)
                    return majority_l;
            }
            if (nums[i] == majority_r)
            {
                temp_r ++;
                if (temp_r > nums.size()/2)
                    return majority_r;
            }
        }
        return 0;
    }
};
