class Solution {
public:
    string getPermutation(int n, int k) {
        k -= 1;
        vector <int> nums;
        string res = "";
        for (int i = 1; i <= n; i++)
            nums.push_back(i);
        while (n > 0)
        {
            int temp = factorial(n-1);
            res += to_string(nums[k/temp]);
            nums.erase(nums.begin() + k/temp);
            k %= temp;
            n -= 1;
        }
        return res;
    }
    int factorial(int n)
    {
        int ret = 1;
        for(int i = 1; i <= n; ++i)
            ret *= i;
        return ret;
    }
};
