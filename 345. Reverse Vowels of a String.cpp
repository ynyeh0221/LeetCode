class Solution {
public:
    bool vowel(char c)
    {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
            return true;
        return false;
    }
    string reverseVowels(string s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r)
        {
            if (vowel(s[l]) && vowel(s[r]))
            {
                char temp = s[l];
                s[l] = s[r];
                s[r] = temp;
            }
            else
            {
                if (vowel(s[l]))
                    l--;
                if (vowel(s[r]))
                    r++;
            }
            l ++;
            r --;
        }
        return s;
    }
};
