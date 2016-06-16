#include <cmath>
class Solution {
public:
    vector<int> grayCode(int n) {
        vector <int> res (1);
        for (int i = 0; i < n; i++)
        {
            vector <int> temp;
            for (int j = 0; j < res.size(); j++)
                temp.push_back(res[j]);
            for (int j = res.size() - 1; j >= 0; j--)
                temp.push_back(res[j] + pow(2, i));
            res = temp;
        }
        return res;
    }
};
