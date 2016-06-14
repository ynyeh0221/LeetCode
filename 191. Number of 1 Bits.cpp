#include <bitset>
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        string binary = bitset<32>(n).to_string();
        for (int i = 0; i<binary.length(); i++)
            res += (binary[i] - '0');
        return res;
    }
};
