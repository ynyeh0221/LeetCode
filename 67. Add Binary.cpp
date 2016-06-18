class Solution {
private:
    string res = "";
    int carry = 0;
public:
    string addBinary(string a, string b) {
        reverse(a.begin(), a.end());
        reverse(b.begin(), b.end());
        int maxlength = a.length() > b.length() ? a.length() : b.length();
        for (int i = 0; i < maxlength; i++)
        {
            if (i < a.length() && i < b.length())
                add(a[i], b[i]);
            else if (i < a.length() && i >= b.length())
                add(a[i], '0');
            else if (i >= a.length() && i < b.length())
                add('0', b[i]);
        }
        if (carry == 1)
            res = to_string(carry) + res;
        return res;
    }
    
    void add(char a, char b)
    {
        int temp = (a - '0') + (b - '0') + carry;
        if (temp >= 2)
        {
            res = to_string(temp - 2) + res;
            carry = 1;
        }
        else
        {
            res = to_string(temp) + res;
            carry = 0;
        }
    }
};
