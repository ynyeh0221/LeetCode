class Solution {
public:
    string reverseString(string s) {
        string res = "";
        for (int i = s.length()-1; i>=0; i--)
            res += s[i];
        return res;
    }
};
