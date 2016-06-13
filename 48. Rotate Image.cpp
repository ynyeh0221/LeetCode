class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.size() > 1)
        {
            reverse(matrix.begin(), matrix.end());
            for (int i = 0; i < matrix.size(); i++)
            {
                for (int j = i + 1; j < matrix[0].size(); j++)
                {
                    int temp = matrix[i][j];
                    matrix[i][j] = matrix[j][i];
                    matrix[j][i] = temp;
                }
            }
        }
    }
};
