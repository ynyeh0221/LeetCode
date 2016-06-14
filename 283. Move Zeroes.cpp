class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int i = 0;
        int length = nums.size();
        while (i < length)
        {
            if (nums[i] == 0)
            {
                nums.erase(nums.begin() + i);
                nums.push_back(0);
                length --;
            }
            else
                i ++;
        }
    }
};
