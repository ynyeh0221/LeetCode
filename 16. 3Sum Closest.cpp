#include <climits>
#include <cmath>
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = 0;
        int difference = INT_MAX;
        int i = 0;
        
        while (i < nums.size())
        {
            int j = i + 1;
            int k = nums.size() - 1;
            while(j < k)
            {
                int temp = nums[i] + nums[j] + nums[k];
                if ( temp == target)
                {
                    return target;
                }
                else if (temp > target)
                {
                    k--;
                    while (k > 0 && k < nums.size() && nums[k] == nums[k+1])
                        k--;
                    if ( abs(temp-target) < difference )
                    {
                        res = temp;
                        difference = abs(temp-target);
                    }
                }
                else
                {
                    j++;
                    while (j > 0 && j < nums.size() && nums[j] == nums[j-1])
                        j++;
                    if ( abs(temp-target) < difference )
                    {
                        res = temp;
                        difference = abs(temp-target);
                    }
                }
            }
            i++;
            while (i < nums.size() && nums[i] == nums[i-1])
                i++;
        }
        return res;
    }
};
