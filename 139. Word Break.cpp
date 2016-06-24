class Solution {
public:
    bool wordBreak(string s, unordered_set<string>& wordDict) {
        vector <bool> T (s.length()+1, false);
        T[0] = true;
        for (int i = 1; i < s.length()+1; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (T[j] && wordDict.count(s.substr(j, i - j)) > 0)
                    T[i] = true;
            }
        }
        return T[s.length()];
    }
};
