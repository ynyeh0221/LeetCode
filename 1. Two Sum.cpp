class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> dic;
        vector <int> res;
        for (int i = 0; i < nums.size(); i++)
        {
            if ( dic.count(nums[i]) == 0 )
                dic[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if ( dic.count( target-nums[i] ) > 0 && i > dic[target-nums[i]] )
            {
                res.push_back( i );
                res.push_back( dic[target-nums[i]] );
                return res;
            }   
        }
        return res;
    }
};
