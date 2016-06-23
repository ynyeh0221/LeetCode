#include <unordered_map>
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        long long int n = numerator;
        long long int d = denominator;
        if (n == 0) return to_string(0);
        int flag = 1;
        if (n < 0)
        {
            n = -n;
            flag *= -1;
        }
        if (d < 0)
        {
            d = -d;
            flag *= -1;
        }
        if (n % d == 0)
            return flag == 1 ? to_string(n / d) : '-' + to_string(n / d);
        string res = to_string(n / d) + ".";
        unordered_map <int, int> dic;
        n = (n % d) * 10;
        while (n > 0)
        {
            if (dic.count(n) == 0)
            {
                dic[n] = res.length();
                res += to_string(n / d);
            }
            else
            {
                char temp = '(';
                res.insert(dic[n], ToStr(temp));
                res += ')';
                break;
            }
            n = (n % d) * 10;
        }
        return flag == 1 ? res : '-' + res;
    }
    string ToStr( char c ) {
        return string( 1, c );
    }
};
