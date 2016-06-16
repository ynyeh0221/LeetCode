#include <unordered_map>
#include <cmath>
class Solution {
public:
    bool isHappy(int n) {
        unordered_map <int, int> dic;
        int sum = n;
        while (true)
        {
            string sumlist = to_string(sum);
            sum = 0;
            for (int i = 0; i < sumlist.length(); i++)
                sum += pow(sumlist[i] - '0', 2);
            if (sum == 1)
                return true;
            if (dic.count(sum) > 0)
                return false;
            dic[sum] = 1;
        }
    }
};
