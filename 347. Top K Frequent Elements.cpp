#include <unordered_map>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> dic;
        for (int i = 0; i<nums.size(); i++)
        {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = 0;
            dic[nums[i]] += 1;
        }
        vector<pair<int, int>> vtMap;
        for (auto it = dic.begin(); it != dic.end(); it++)
            vtMap.push_back(make_pair(it->first, it->second));

        sort(vtMap.begin(), vtMap.end(), 
        [](const pair<int, int> &x, const pair<int, int> &y) -> int {
        return x.second > y.second;
        });
        
        vector<int> res;
        for (auto it = vtMap.begin(); it != vtMap.begin() + k; it++)
            res.push_back(it->first);
        return res;
    }
};
