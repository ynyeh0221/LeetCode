#include <cmath>
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        if (n == 0)
            return {};
        vector<vector<int>> matrix;
        for (int i = 0; i < n; i++)
        {
            vector <int> row;
            for (int j = 0; j < n; j++)
                row.push_back(pow(n, 2));
            matrix.push_back(row);
        }
        int current_n = 1;
        DFS(matrix, current_n, n, 0, 0, 0, n-1, 1, n-1, 0);
        return matrix;
    }
    
    void DFS(vector<vector<int>> &matrix, int &current_n, int n, int i, int j, int xmin, int xmax, int ymin, int ymax, int direction)
    {
        if (current_n == pow(n, 2))
            return;
        if (direction == 0)
        {
            while (j < xmax)
            {
                matrix[i][j] = current_n;
                j ++;
                current_n ++;
            }
            DFS(matrix, current_n, n, i, j, xmin, xmax-1, ymin, ymax, 1);
        }
        else if (direction == 1)
        {
            while (i < ymax)
            {
                matrix[i][j] = current_n;
                i ++;
                current_n ++;
            }
            DFS(matrix, current_n, n, i, j, xmin, xmax, ymin, ymax-1, 2);
        }
        else if (direction == 2)
        {
            while (j > xmin)
            {
                matrix[i][j] = current_n;
                j --;
                current_n ++;
            }
            DFS(matrix, current_n, n, i, j, xmin+1, xmax, ymin, ymax, 3);
        }
        else if (direction == 3)
        {
            while (i > ymin)
            {
                matrix[i][j] = current_n;
                i --;
                current_n ++;
            }
            DFS(matrix, current_n, n, i, j, xmin, xmax, ymin+1, ymax, 0);
        }
    }
};
