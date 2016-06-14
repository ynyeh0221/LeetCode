class Solution {
public:
    bool isPowerOfFour(int num) {
        return num > 0 && int(log10(num) / log10(4)) == log10(num) / log10(4) ? true : false;
    }
};
