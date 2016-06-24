// timeout

class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";
        if (s.length() > 0) res = s[0];
        vector <vector <bool>> T (s.length(), vector <bool> (s.length(), false));
        for (int i = 0; i < s.length(); i++)
        {
            for (int j = 0; j < i; j++)
            {
                T[j][i] = (s[j] == s[i] && (i-j<2 || T[j+1][i-1]));
                if (T[j][i] && res.length() < i-j+1)
                    res = s.substr(j, i-j+1);
            }
            T[i][i] = true;
        }
        return res;
    }
};
