class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        for (int i = 0; i<nums.size(); i++)
        {
            if (nums[i] == target)
                return i;
            else
            {
                if (target < nums[0])
                    return 0;
                else if (target > nums[nums.size() - 1])
                    return nums.size();
                else if (i > 0 && nums[i-1] < target && nums[i] > target)
                    return i;
            }
        }
        return 0;
    }
};
