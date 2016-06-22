class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int i = 0, start = 0, sum = 0, totalsum = 0;
        while (i < gas.size())
        {
            sum += gas[i] - cost[i];
            totalsum += gas[i] - cost[i];
            if (sum < 0)
            {
                sum = 0;
                start = i + 1;
            }
            i ++;
        }
        return totalsum < 0 ? -1 : start;
    }
};
