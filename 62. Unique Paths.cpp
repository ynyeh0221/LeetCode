class Solution {
public:
    int uniquePaths(int m, int n) {
        vector <vector<int>> T;
        for (int i = 0; i < m; i++)
        {
            vector <int> row;
            if (i == 0)
            {
                for (int j = 0; j < n; j++)
                    row.push_back(1);
            }
            else
            {
                row.push_back(1);
                for (int j = 1; j < n; j++)
                    row.push_back(0);
            }
            T.push_back(row);
        }
        for (int i = 1; i < m; i++)
        {
            for (int j = 1; j < n; j++)
                T[i][j] = T[i-1][j] + T[i][j-1];
        }
        return T[m-1][n-1];
    }
};
