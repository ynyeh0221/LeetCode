class Solution {
private:
    vector<vector<string>> res;
public:
    vector<vector<string>> solveNQueens(int n) {
        DFS({}, n);
        return res;
    }
    bool check(vector <int> path, int i)
    {
        for (int j = 0; j < path.size(); j++)
        {
            if (path[j] == i || path.size() - j == abs(path[j] - i))
                return false;
        }
        return true;
    }
    void DFS(vector <int> path, int& n)
    {
        if (path.size() == n)
        {
            vector <string> board;
            for (int i = 0; i < path.size(); i++)
            {
                string row = "";
                for (int j = 0; j < n; j++)
                {
                    if (j != path[i])
                        row += '.';
                    else
                        row += 'Q';
                }
                board.push_back(row);
            }
            res.push_back(board);
            return;
        }
        for (int i = 0; i < n; i++)
        {
            if (check(path, i))
            {
                path.push_back(i);
                DFS(path, n);
                path.pop_back();
            }
        }
    }
};
