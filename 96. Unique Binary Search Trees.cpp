class Solution {
public:
    int numTrees(int n) {
        if (n == 0 || n == 1) return 1;
        vector <int> T (n+1);
        T[0] = 1; T[1] = 1;
        for (int i = 2; i <= n; i++)
        {
            for (int j = 1; j <= i; j++)
                T[i] += T[j-1] * T[i-j];
        }
        return T[n];
    }
};
