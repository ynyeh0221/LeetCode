class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        
        int i=0;
        while (i < nums.size())
        {
            int j = i + 1;
            while (j < nums.size())
            {
                int k = j+1;
                int l = nums.size()-1;
                while (k < l)
                {
                    if (nums[i]+nums[j]+nums[k]+nums[l] == target)
                    {
                        vector<int> temp {nums[i], nums[j], nums[k], nums[l]};
                        res.push_back(temp);
                        k++;
                        l--;
                        while (k < nums.size() && nums[k] == nums[k-1])
                            k++;
                        while (l > j && nums[l] == nums[l+1])
                            l--;
                    }
                    else if (nums[i]+nums[j]+nums[k]+nums[l] > target)
                    {
                        l--;
                        while (l > j && nums[l] == nums[l+1])
                            l--;
                    }
                    else
                    {
                        k++;
                        while (k < nums.size() && nums[k] == nums[k-1])
                            k++;
                    }
                }
                j++;
                while (j < nums.size() and nums[j] == nums[j-1])
                    j++;
            }
            i++;
            while (i < nums.size() and nums[i] == nums[i-1])
                i++;
        }
        return res;
    }
};
