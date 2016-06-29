class Solution {
public:
    int search(vector<int>& nums, int target) {
        int temp = nums[0];
        if (target == temp) return 0;
        else if (target > temp)
        {
            for (int i = 0; i < nums.size(); i++)
            {
                if (nums[i] < temp) return -1;
                if (target == nums[i]) return i;
            }
        }
        else
        {
            for (int i = nums.size()-1; i >= 0; i--)
            {
                if (nums[i] > temp) return -1;
                if (target == nums[i]) return i;
            }
        }
        return -1;
    }
};
