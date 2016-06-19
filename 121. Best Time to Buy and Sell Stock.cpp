#include <climits>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0) return 0;
        int maxx = -INT_MAX;
        int end = 0;
        int start = prices[0];
        for (int i = 1; i < prices.size(); i++)
        {
            end = prices[i];
            maxx = max(maxx, end - start);
            start = min(start, end);
        }
        return maxx > 0 ? maxx : 0;
    }
};
