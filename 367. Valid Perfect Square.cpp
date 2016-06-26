class Solution {
public:
    bool isPerfectSquare(int num) {
        long long int l = 0, r = (int)(num/2 + 1);
        while (l <= r)
        {
            long long int mid = (l+r) >> 1;
            if (mid*mid == num) return true;
            else if (mid*mid < num)
                l = mid + 1;
            else
                r = mid - 1;
        }
        return false;
    }
};
