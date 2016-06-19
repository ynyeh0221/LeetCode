#include <unordered_map>
class Solution {
public:
    string getHint(string secret, string guess) {
        unordered_map <int, int> A, dic;
        for (int i = 0; i < secret.length(); i++)
        {
            if (secret[i] == guess[i])
                A[i] = 1;
            else
            {
                if (dic.count(secret[i]) == 0) dic[secret[i]] = 0;
                dic[secret[i]] ++;
            }
        }
        int numB = 0;
        for (int i = 0; i < guess.length(); i++)
        {
            if (dic.count(guess[i]) > 0 && dic[guess[i]] > 0 && A.count(i) == 0)
            {
                numB ++;
                dic[guess[i]] --;
            }
        }
        return to_string(A.size()) + 'A' + to_string(numB) + 'B';
    }
};
