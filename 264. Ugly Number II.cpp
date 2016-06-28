#include <unordered_map>
class Solution {
public:
    int min(int a, int b, int c)
    {
        int temp = a < b ? a : b;
        return temp < c ? temp : c;
    }
    int nthUglyNumber(int n) {
        vector <int> res {1};
        int ind2 = 0, ind3 = 0, ind5 = 0;
        unordered_map <int, int> dic;
        while (res.size() < n)
        {
            int minn = 0;
            minn = min(2*res[ind2], 3*res[ind3], 5*res[ind5]);
            if (minn == 2*res[ind2])
            {
                minn = 2*res[ind2];
                ind2 ++;
            }
            else if (minn == 3*res[ind3])
            {
                minn = 3*res[ind3];
                ind3 ++;
            }
            else
            {
                minn = 5*res[ind5];
                ind5 ++;
            }
            if (dic.count(minn) == 0)
            {
                res.push_back(minn);
                dic[minn] = 1;
            }
        }
        return res[n-1];
    }
};
