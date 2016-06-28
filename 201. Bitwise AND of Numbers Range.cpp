#include <bitset>
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        string bin_m = bitset <32> (m).to_string();
        string bin_n = bitset <32> (n).to_string();
        int res = 0;
        for (int i = bin_m.length()-1; i >= 0; i--)
        {
            bool equal = true;
            for (int j = 0; j <= i; j++)
            {
                if (bin_m[j] != bin_n[j])
                {
                    equal = false;
                    break;
                }
            }
            if (equal)
            {
                for (int j = 0; j <= i; j++)
                    res += (bin_m[j]-'0') * pow(2, bin_m.size() - 1 - j);
                break;
            }
        }
        return res;
    }
};
