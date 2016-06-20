class Solution {
public:
    int titleToNumber(string s) {
        int base = 1;
        int res = 0;
        for (int i = s.size()-1; i >= 0; i--)
        {
            res += (s[i] - 'A' +1) *base;
            base *= 26;
        }
        return res;
    }
};
