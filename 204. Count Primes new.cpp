class Solution {
public:
    int countPrimes(int n) {
        if(n == 0 || n == 1) return 0;
        vector <int> T (n, 1);
        T[0] = 0, T[1] = 0;
        for (int i = 2; i*i < n; i++)
        {
            for (int j = i*i; j < n; j = j + i) T[j] = 0;
        }
        int res = 0;
        for (int i = 0; i < n; i++)
            res += T[i];
        return res;
    }
};
