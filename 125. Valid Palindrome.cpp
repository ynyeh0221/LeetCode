class Solution {
public:
    bool isPalindrome(string s) {
        for (int i = 0; i < s.length(); i++)
            s[i] = tolower(s[i]);
        int start = 0;
        int end = s.length() - 1;
        while (start <= end)
        {
            if (isalnum(s[start]) && isalnum(s[end]))
            {
                if (s[start] != s[end])
                    return false;
                start ++;
                end --;
            }
            else
            {
                if (!isalnum(s[start]))
                    start ++;
                else
                    end --;
            }
        }
        return true;
    }
};
