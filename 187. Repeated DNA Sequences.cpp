#include <unordered_map>
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if (s.length() < 10) return {};
        unordered_map <string, int> dic;
        vector <string> res;
        for (int i = 0; i < s.length() - 9; i++)
        {
            string temp = s.substr(i, 10);
            if (dic.count(temp) > 0)
            {
                dic[temp]++;
                if (dic[temp] == 2) res.push_back(temp);
            }
            else
                dic[temp] = 1;
        }
        return res;
    }
};
