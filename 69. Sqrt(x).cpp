class Solution {
public:
    int mySqrt(int x) {
        long long int l = 0;
        long long int r = x/2 + 1;
        while (l <= r)
        {
            long long int mid = (int)((l+r) / 2);
            if (mid*mid == x)
                return mid;
            else if (mid*mid < x)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return r;
    }
};
