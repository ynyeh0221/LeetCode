class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        if (n == 1) return 10;
        int res = 10;
        for (int i = 1; i < n; i++)
        {
            int temp = 9;
            for (int j = 9; j > 9-i; j--)
                temp *= j;
            res += temp;
        }
        return res;
    }
};
