class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        vector <int> freq1 (26);
        vector <int> freq2 (26);
        
        for (int i = 0; i < s.length(); i++)
        {
            freq1[s[i] - 'a'] ++;
            freq2[t[i] - 'a'] ++;
        }
        return equal(freq1.begin(), freq1.begin() + 26, freq2.begin()) ? true : false;
    }
};
