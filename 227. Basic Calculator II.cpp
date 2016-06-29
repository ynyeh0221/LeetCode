class Solution {
public:
    int calculate(string s) {
    int result = 0, num = 0, temp = 0;
    char op = '+';
    for (int i = 0; i < s.length(); i++)
    {
        if (isdigit(s[i]))
        {
            num = 0;
            while (i < s.length() && isdigit(s[i]))
            {
                num = num * 10 + s[i] - '0';
                i++;
            }
            if (op == '+' || op == '-')
            {
                result += temp;
                temp = num * (op == '-' ? -1 : 1);
            }
            else if (op == '*')
                temp *= num;
            else if (op == '/')
                temp /= num;
        }
        if (s[i] != ' ')
            op = s[i];
    }
    result += temp;
    return result;
    }
};
