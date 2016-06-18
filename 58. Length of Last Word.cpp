#include <stringstream>
class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0;
        int length = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] != ' ')
                length ++;
            else
            {
                if (length > 0)
                {
                    res = length;
                    length = 0;
                }
            }
        }
        if (length > 0)
            res = length;
        return res == 0 ? 0 : res;
    }
};
