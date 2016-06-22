class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        vector<int> temp = nums;
        sort(temp.begin(), temp.end());
        int s = (int) ((nums.size() + 1) / 2);
        int l = nums.size();
        for (int i = 0; i < nums.size(); i++)
        {
            if (i % 2 == 0)
            {
                s--;
                nums[i] = temp[s];
            }
            else
            {
                l--;
                nums[i] = temp[l];
            }
        }
    }
};
