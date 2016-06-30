class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int ind1 = nums.size()-1, ind2 = nums.size()-1;
        for (int i = nums.size()-1; i >= 0; i--)
        {
            if (nums[i] > nums[i-1])
            {
                ind1 = i-1;
                break;
            }
        }
        int min = INT_MAX;
        for (int i = ind1+1; i < nums.size(); i++)
        {
            if (nums[i] < min && nums[i] > nums[ind1])
            {
                min = nums[i];
                ind2 = i;
            }
        }
        if (ind1 == -1)
            sort(nums.begin(), nums.end());
        else
        {
            int t = nums[ind1];
            nums[ind1] = nums[ind2];
            nums[ind2] = t;
            vector <int> temp (nums.begin() + ind1 + 1, nums.end());
            sort(temp.begin(), temp.end());
            for (int i = ind1 + 1; i < nums.size(); i++)
                nums[i] = temp[i-ind1-1];
        }
    }
};
