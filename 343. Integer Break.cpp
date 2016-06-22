class Solution {
public:
    int integerBreak(int n) {
        if (n == 2) return 1;
        if (n == 3) return 2;
        if (n == 4) return 4;
        if (n == 5) return 6;
        if (n == 6) return 9;
        vector <int> T (n+1);
        T[4] = 4; T[5] = 6; T[6] = 9;
        for (int i = 7; i <= n; i++)
            T[i] = T[i-3] * 3;
        return T[n];
    }
};
