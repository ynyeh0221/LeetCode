#include <unordered_map>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map <char, char> dic_s, dic_t;
        for (int i = 0; i < s.length(); i++)
        {
            if (dic_s.count(s[i]) == 0 && dic_t.count(t[i]) == 0)
            {
                dic_s[s[i]] = t[i];
                dic_t[t[i]] = s[i];
            }
            else if (dic_s.count(s[i]) > 0 && dic_t.count(t[i]) > 0)
            {
                if (dic_s[s[i]] != t[i] || dic_t[t[i]] != s[i]) return false;
            }
            else
                return false;
        }
        return true;
    }
};
