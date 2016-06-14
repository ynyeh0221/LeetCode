#include <algorithm> 
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0)
            return 0;
        vector<int> T (amount + 1, amount + 1);
        T[0] = 0;
        for(int a = 1; a < amount + 1; a++)
        {
            for (int c = 0; c < coins.size(); c++)
            {
                if (coins[c] <= a)
                    T[a] = min(T[a - coins[c]] + 1, T[a]);
            }
        }
        return T[amount] == amount + 1 ? -1 : T[amount];
    }
};
