class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int i=0;
        
        while (i < nums.size())
        {
            int j = i + 1;
            int k = nums.size() - 1;
            while(j < k)
            {
                if (nums[i] + nums[j] + nums[k] == 0)
                {
                    vector <int> temp {nums[i], nums[j], nums[k]};
                    res.push_back(temp);
                    j++;
                    k--;
                    while (j > 0 && j < nums.size() && nums[j] == nums[j-1])
                        j++;
                    while (k > 0 && k < nums.size() && nums[k] == nums[k+1])
                        k--;
                }
                else if (nums[i] + nums[j] + nums[k] > 0)
                {
                    k--;
                    while (k > 0 && k < nums.size() && nums[k] == nums[k+1])
                        k--;
                }
                else
                {
                    j++;
                    while (j > 0 && j < nums.size() && nums[j] == nums[j-1])
                        j++;
                }
            }
            i++;
            while (i > 0 && i < nums.size() && nums[i] == nums[i-1])
                i++;
        }
        return res;
    }
};
