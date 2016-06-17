class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> combine(int n, int k) {
        vector <int> path;
        combination(1, path, n, k);
        return res;
    }
    
    void combination(int start, vector <int> path, int n, int k)
    {
        if (path.size() == k)
        {
            res.push_back(path);
            return;
        }
        for (int i = start; i <= n; i++)
        {
            path.push_back(i);
            combination(i+1, path, n, k);
            path.pop_back();
        }
    }
};
