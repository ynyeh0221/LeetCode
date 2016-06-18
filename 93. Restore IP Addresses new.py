#include <sstream>
class Solution {
private:
    vector <string> res;
public:
    vector<string> restoreIpAddresses(string s) {
        if (s.size() < 4 || s.size() > 12) return {};
        DFS(0, {}, s);
        return res;
    }
    
    void DFS(int start, vector <string> path, string s)
    {
        if (start > s.length()) return;
        if (start == s.length())
        {
            if (path.size() == 4)
            {
                stringstream ss;
                for(size_t i = 0; i < path.size(); ++i)
                {
                    if(i != 0)
                    ss << ".";
                    ss << path[i];
                }
                res.push_back(ss.str());
            }
            return;
        }
        if (s.length() - start > 3 * (4 - path.size())) return;
        if (s.length() - start < 4 - path.size()) return;
        for (int j = 1; j < 4; j++)
        {
            if (j > 1 && s[start] == '0') return;
            string temp = s.substr(start, j);
            if (stoi(temp) >= 0 && stoi(temp) <= 255)
            {
                path.push_back(temp);
                DFS(start + j, path, s);
                path.pop_back();
            }
        }
    }
};
