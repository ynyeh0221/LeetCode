#include <climits>
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<vector<int>> T;
        for (int i = 0; i < triangle.size(); i++)
        {
            vector <int> row;
            for (int j = 0; j < triangle[i].size(); j++)
                row.push_back(0);
            T.push_back(row);
        }
        T[0][0] = triangle[0][0];
        for (int i = 1; i < triangle.size(); i++)
        {
            for (int j = 0; j < triangle[i].size(); j++)
            {
                if (j > 0 && j < triangle[i-1].size())
                {
                    if (T[i-1][j] + triangle[i][j] < T[i-1][j-1] + triangle[i][j])
                        T[i][j] = T[i-1][j] + triangle[i][j];
                    else
                        T[i][j] = T[i-1][j-1] + triangle[i][j];
                }
                else
                {
                    if (j == 0)
                        T[i][j] = T[i-1][j] + triangle[i][j];
                    else
                        T[i][j] = T[i-1][j-1] + triangle[i][j];
                }
            }
        }
        int minn = INT_MAX;
        for(int i = 0; i < T[T.size()-1].size(); i++)
        {
            if (T[T.size()-1][i] < minn)
                minn = T[T.size()-1][i];
        }
        return minn;
    }
};
