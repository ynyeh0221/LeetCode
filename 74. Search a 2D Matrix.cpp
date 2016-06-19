class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for (int i = 0; i < matrix.size(); i++)
        {
            if (target >= matrix[i][0] && target <= matrix[i][matrix[i].size() - 1])
                return find(matrix[i].begin(), matrix[i].end(), target) != matrix[i].end() ? true : false;
        }
        return false;
    }
};
