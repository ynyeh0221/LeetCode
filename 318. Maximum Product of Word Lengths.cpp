class Solution {
public:
    int maxProduct(vector<string>& words) {
        vector <vector<int>> wordlist;
        int res = 0;
        for (int i = 0; i < words.size(); i++)
        {
            vector <int> letters (26);
            for (int j = 0; j < words[i].size(); j++)
                letters[words[i][j] - 'a'] = 1;
            wordlist.push_back(letters);
        }
        for (int i = 0; i < wordlist.size(); i++)
        {
            for (int j = i+1; j < wordlist.size(); j++)
            {
                int difference = 0;
                for (int k = 0; k < 26; k++)
                {
                    if (wordlist[i][k] == 1 && wordlist[j][k] == 1)
                        break;
                    else
                        difference ++;
                }
                if (difference == 26)
                    res = res > words[i].size() * words[j].size() ? res : words[i].size() * words[j].size();
            }
        }
        return res;
    }
};
