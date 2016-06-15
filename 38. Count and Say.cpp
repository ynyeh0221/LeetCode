#include <string>
class Solution {
public:
    string countAndSay(int n) {
        string res = "1";
        for (int i = 1; i < n; i++)
        {
            string temp = "";
            int c = 0;
            for (int j = 0; j < res.length(); j++)
            {
                if (j == 0)
                    c ++;
                else
                {
                    if (res[j] != res[j-1])
                    {
                        temp += to_string(c) + res[j-1];
                        c = 1;
                    }
                    else
                        c++;
                }
            }
            temp += to_string(c) + res[res.length()-1];
            res = temp;
        }
        return res;
    }
};
