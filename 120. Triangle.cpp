// timeout

#include <climits>
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int res = INT_MAX;
        vector <int> path;
        DFS(triangle, path, res, 0, 0);
        return res;
    }
    
    void DFS(vector<vector<int>>& triangle, vector <int> path, int &res, int location, int level)
    {
        if (path.size() == triangle.size())
        {
            int sum = accumulate(path.begin(), path.end(), 0);
            if (sum < res)
                res = sum;
            return;
        }
        if (location < triangle[level].size())
        {
            path.push_back(triangle[level][location]);
            DFS(triangle, path, res, location, level + 1);
            path.pop_back();
        }
        if (location + 1 < triangle[level].size())
        {
            path.push_back(triangle[level][location + 1]);
            DFS(triangle, path, res, location + 1, level + 1);
            path.pop_back();
        }
    }
};
