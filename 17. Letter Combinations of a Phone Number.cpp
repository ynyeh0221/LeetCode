class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        vector<char> path;
        if (digits.size() == 0)
            return {};
        vector<vector<char>> buttons {{},{},{'a','b','c'},{'d','e','f'},{'g','h','i'},{'j','k','l'},{'m','n','o'},{'p','q','r','s'},{'t','u','v'},{'w','x','y','z'}};
        DFS(buttons, digits, path, res);
        return res;
    }
    
    void DFS(vector<vector<char>> buttons, string digits, vector<char> path, vector<string>& res)
    {
        if (path.size() == digits.size())
        {
            string temp = "";
            for (int i = 0; i < path.size(); i++)
                temp += path[i];
            res.push_back(temp);
            return;
        }
        for (int i = 0; i < digits.size(); i++)
        {
            if (path.size() == i)
            {
                for (int j = 0; j < buttons[digits[i] - '0'].size(); j++)
                {
                    path.push_back(buttons[digits[i] - '0'][j]);
                    DFS(buttons, digits, path, res);
                    path.pop_back();
                }
            }
        }
    }
};
