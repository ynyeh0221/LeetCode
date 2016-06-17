class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.size() == 0)
            return {};
        vector<string> res;
        int begin = nums[0], end = nums[0];
        for(int i = 1; i < nums.size(); i++)
        {
            if (nums[i] == end + 1)
                end = nums[i];
            else
            {
                if (begin != end)
                    res.push_back(to_string(begin) + "->" +to_string(end));
                else
                    res.push_back(to_string(begin));
                begin = nums[i];
                end = nums[i];
            }
        }
        if (begin != end)
            res.push_back(to_string(begin) + "->" +to_string(end));
        else
            res.push_back(to_string(begin));
        return res;
    }
};
