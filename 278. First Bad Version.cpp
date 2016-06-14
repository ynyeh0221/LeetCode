// timeout

// Forward declaration of isBadVersion API.
bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        while (start <= end)
        {
            int mid = (start + end)/2;
            if (!isBadVersion(mid))
                start = mid + 1;
            else
                end = mid - 1;
        }
        return start;
    }
};
