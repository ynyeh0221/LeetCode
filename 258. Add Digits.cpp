class Solution {
public:
    int addDigits(int num) {
        return num == 0 ? 0 : num - 9 * int((num-1) / 9);
    }
};
