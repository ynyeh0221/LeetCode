class Solution {
public:
    int numDecodings(string s) {
        char zero = '0';
        if (s.length() == 0 || s[0] == zero) return 0;
        vector <int> T (s.length());
        T[0] = 1;
        if (s.length() > 1)
        {
            if (stoi(s.substr(0,2)) <= 26 && s[1] != zero)
                T[1] = 2;
            else if ((stoi(s.substr(0,2)) <= 26 && s[1] == zero) || (stoi(s.substr(0,2)) > 26 && s[1] != zero))
                T[1] = 1;
            else
                return 0;
        }
        for (int i = 2; i < s.length(); i++)
        {
            if (s[i] == zero && s[i-1] == zero) return 0;
            else if (s[i] != zero && s[i-1] != zero)
            {
                T[i] += T[i-1];
                if (stoi(s.substr(i-1,2)) <= 26)
                    T[i] += T[i-2];
            }
            else if (s[i] == zero && s[i-1] != zero)
            {
                if (stoi(s.substr(i-1,2)) <= 26)
                    T[i] += T[i-2];
                else
                    return 0;
            }
            else
                T[i] += T[i-1];
        }
        return T[s.length()-1];
    }
};
