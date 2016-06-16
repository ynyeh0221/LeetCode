class Solution {
public:
    bool isPalindrome(int x) {
        if (x >= 0 && x / 10 == 0)
            return true;
        if (x >= 0 && x % 10 == 0) // 10, 100, ...
            return false;
        int temp = 0;
        while (x > 0)
        {
            temp = temp * 10 + x % 10;
            if (x == temp || x / 10 == temp) //total digits is odd or even
                return true;
            x /= 10;
        }
        return false;
    }
};
