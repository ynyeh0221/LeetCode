class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector <vector<int>> T (m+1, vector<int>(n+1));
        for (int i = 1; i <= m; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                if (i == 1) T[1][j] = T[1][j-1] + grid[0][j-1];
                else if (j == 1) T[i][1] = T[i-1][1] + grid[i-1][0];
                else
                    T[i][j] = T[i-1][j] + grid[i-1][j-1] < T[i][j-1] + grid[i-1][j-1] ? T[i-1][j] + grid[i-1][j-1] : T[i][j-1] + grid[i-1][j-1];
            }
        }
        return T[m][n];
    }
};
