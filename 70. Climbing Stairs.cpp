class Solution {
public:
    int climbStairs(int n) {
        vector <int> T (n + 1);
        if (n >= 1)
            T[1] = 1;
        if (n >= 2)
            T[2] = 2;
        for (int i = 3; i <= n; i++)
            T[i] = T[i-1] + T[i-2];
        return T[n];
    }
};
