#include <set>
class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        set <int> s;
        for (int i = 0; i < nums.size(); i++)
        {
            if (s.count(nums[i]) > 0)
                s.erase(nums[i]);
            else
                s.insert(nums[i]);
        }
        vector <int> res;
        copy(s.begin(), s.end(), back_inserter(res));
        return res;
    }
};
