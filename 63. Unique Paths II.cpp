class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector <vector<int>> T;
        for (int i = 0; i < m; i++)
        {
            vector <int> row;
            for (int j = 0; j < n; j++)
                row.push_back(0);
            T.push_back(row);
        }
        for (int i = 0; i < m; i++)
        {
            if (obstacleGrid[i][0] == 0)
                T[i][0] = 1;
            else
                break;
        }
        for (int j = 0; j < n; j++)
        {
            if (obstacleGrid[0][j] == 0)
                T[0][j] = 1;
            else
                break;
        }
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
            {
                if (obstacleGrid[i][j] == 0)
                    T[i][j] = T[i-1][j] + T[i][j-1];
            }
        }
        return T[m-1][n-1];
    }
};
