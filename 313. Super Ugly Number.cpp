class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        vector <long long int> candidates (primes.size(), 1);
        vector <int> inds (primes.size());
        vector <long long int> res {1};
        long long int minn = 1;
        while (res.size() < n)
        {
            for (int i = 0; i < primes.size(); i++)
            {
                if (minn == candidates[i])
                {
                    candidates[i] = primes[i] * res[inds[i]];
                    inds[i] ++;
                }
            }
            int temp = INT_MAX;
            for (int j = 0; j < primes.size(); j++)
            {
                if (candidates[j] < temp)
                    temp = candidates[j];
            }
            minn = temp;
            res.push_back(minn);
        }
        return res[n - 1];
    }
};
