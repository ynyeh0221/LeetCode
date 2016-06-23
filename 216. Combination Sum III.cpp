class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        DFS({}, 1, k, n);
        return res;
    }
    void DFS(vector <int> path, int start, int k, int n)
    {
        if (path.size() == k || n == 0 || start == 10)
        {
            if (path.size() == k && n == 0)
            {
                res.push_back(path);
                return;
            }
        }
        for (int i = start; i <= 9; i++)
        {
            if (i <= n)
            {
                path.push_back(i);
                DFS(path, i + 1, k, n - i);
                path.pop_back();
            }
        }
    }
};
