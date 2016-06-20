#include <unordered_map>
class Solution {
public:
    int romanToInt(string s) {
        unordered_map <char, int> nums;
        nums['I'] = 1;
        nums['V'] = 5;
        nums['X'] = 10;
        nums['L'] = 50;
        nums['C'] = 100;
        nums['D'] = 500;
        nums['M'] = 1000;
        int res = nums[s[0]];
        for (int i = 1; i < s.size(); i++)
        {
            if (nums[s[i]] > nums[s[i-1]])
                res += nums[s[i]] - 2*nums[s[i-1]];
            else
                res += nums[s[i]];
        }
        return res;
    }
};
