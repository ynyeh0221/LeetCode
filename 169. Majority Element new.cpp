#include <unordered_map>
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> dic;
        for (int i = 0; i < nums.size(); i++)
        {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = 0;
            dic[nums[i]] ++;
            if (dic[nums[i]] > nums.size() / 2)
                return nums[i];
        }
        return 0;
    }
};
