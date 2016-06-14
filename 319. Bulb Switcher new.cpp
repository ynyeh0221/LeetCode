class Solution {
public:
    int bulbSwitch(int n) {
        int res = 0;
        for (int i = 1; i<=n; i++)
        {
            if (i*i <= n)
                res ++;
            else
                break;
        }
        return res;
    }
};
