#include <stack>
class Solution {
public:
    bool isValid(string s) {
        stack <int> pstack;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
                pstack.push(s[i]);
            else
            {
                if ((s[i] == ')' && (pstack.empty() || pstack.top() != '(')) || (s[i] == ']' && (pstack.empty() || pstack.top() != '[')) || (s[i] == '}' && (pstack.empty() || pstack.top() != '{')))
                    return false;
                else
                    pstack.pop();
            }
        }
        return pstack.empty() ? true : false;
    }
};
