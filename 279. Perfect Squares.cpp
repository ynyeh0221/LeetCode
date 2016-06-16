class Solution {
public:
    int numSquares(int n) {
        vector <int> T (n + 1, n + 1);
        T[0] = 0;
        T[1] = 1;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j * j <= i; j++)
                T[i] = T[i] < T[i - j * j] + 1 ? T[i] : T[i - j * j] + 1;
        }
        return T[n];
    }
};
