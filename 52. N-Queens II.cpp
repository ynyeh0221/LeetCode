class Solution {
private:
    int res = 0;
public:
    int totalNQueens(int n) {
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
            res ++;
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
