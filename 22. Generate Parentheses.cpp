class Solution {
private:
    vector <string> res;
public:
    vector<string> generateParenthesis(int n) {
        DFS(n, n, n, "");
        return res;
    }
    
    void DFS(int left, int right, int n, string path)
    {
        if (path.length() == 2 * n)
        {
            res.push_back(path);
            return;
        }
        if (left == right)
            DFS(left-1, right, n, path + "(");
        else if (left < right)
        {
            for (int i = 0; i < 2; i++)
            {
                if (i == 0)
                    DFS(left, right-1, n, path + ")");
                else
                {
                    if (left > 0)
                        DFS(left-1, right, n, path + "(");
                }
            }
        }
    }
};
