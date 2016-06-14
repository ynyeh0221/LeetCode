#include <string>
#include <algorithm>
class Solution {
public:
    int reverse(int x) {
        try
        {
            int sign = 1;
            if (x < 0)
            {
                x = -x;
                sign = -1;
            }
            string str_x = to_string(x);
            string reverse_str_x = "";
            for (int i = str_x.size()-1; i >= 0; i--)
                reverse_str_x += str_x[i];
            return sign == 1 ? stoi(reverse_str_x) : -stoi(reverse_str_x);
        }
        catch (...)
        {
            return 0;
        }
    }
};
