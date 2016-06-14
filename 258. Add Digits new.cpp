#include <string>
class Solution {
public:
    int addDigits(int num) {
        string str_num = to_string(num);
        while (str_num.size() > 1)
        {
            int sum = 0;
            for (int i = 0; i < str_num.size(); i++)
                sum += str_num[i] - '0';
            str_num = to_string(sum);
        }
        return stoi(str_num);
    }
};
