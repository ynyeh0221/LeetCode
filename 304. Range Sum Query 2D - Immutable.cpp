class NumMatrix {
public:
    vector <vector<int>> T;
    NumMatrix(vector<vector<int>> &matrix) {
        int m = matrix.size();
        if(matrix.empty()) return;
        int n = matrix[0].size();
        T = vector<vector<int>> (m, vector<int>(n));
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(i == 0 && j == 0)
                    T[i][j] = matrix[0][0];
                else if(i == 0)
                    T[i][j] = T[i][j-1] + matrix[i][j];
                else if(j == 0)
                    T[i][j] = T[i-1][j] + matrix[i][j];
                else
                    T[i][j] = T[i-1][j] + T[i][j-1] + matrix[i][j] - T[i-1][j-1];
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        if (row1 == 0 && col1 == 0)
            return T[row2][col2];
        else if (row1 > 0 && col1 == 0)
            return T[row2][col2] - T[row1-1][col2];
        else if (row1 == 0 && col1 > 0)
            return T[row2][col2] - T[row2][col1-1];
        return T[row2][col2] - T[row1-1][col2] - T[row2][col1-1] + T[row1-1][col1-1];
    }
};


// Your NumMatrix object will be instantiated and called as such:
// NumMatrix numMatrix(matrix);
// numMatrix.sumRegion(0, 1, 2, 3);
// numMatrix.sumRegion(1, 2, 3, 4);
