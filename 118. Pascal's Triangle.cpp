class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        if (numRows == 1) return {{1}};
        vector<vector<int>> res {{1}, {1,1}};
        for (int i = 3; i <= numRows; i++)
        {
            vector <int> temp (1,1);
            for (int j = 1; j < res[i - 2].size(); j++)
                temp.push_back(res[i - 2][j - 1] + res[i - 2][j]);
            temp.push_back(1);
            res.push_back(temp);
        }
        return res;
    }
};
