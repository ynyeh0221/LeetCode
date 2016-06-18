#include <stringstream>
class Solution {
public:
    int lengthOfLastWord(string s) {
        vector <int> res;
        int length = 0;
        for (int i = 0; i < s.length(); i++)
        {
            if (s[i] != ' ')
                length ++;
            else
            {
                if (length > 0)
                {
                    res.push_back(length);
                    length = 0;
                }
            }
        }
        if (length > 0)
            res.push_back(length);
        return res.size() == 0 ? 0 : res[res.size() - 1];
    }
};
