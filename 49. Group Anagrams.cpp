#include <unordered_map>
#include <algorithm>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map <string, vector<string>> dic;
        for (int i = 0; i < strs.size(); i++)
        {
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            if (dic.count(temp) == 0)
                dic[temp] = {};
            dic[temp].push_back(strs[i]);
        }
        vector <vector<string>> res;
        for(auto kv : dic)
            res.push_back(kv.second);
        return res;
    }
};
