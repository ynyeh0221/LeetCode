class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if (rowIndex == 0) return {1};
        if (rowIndex == 1) return {1,1};
        vector<int> pre {1,1};
        for (int i = 2; i <= rowIndex; i++)
        {
            vector <int> temp (1,1);
            for (int j = 1; j < pre.size(); j++)
                temp.push_back(pre[j - 1] + pre[j]);
            temp.push_back(1);
            pre = temp;
        }
        return pre;
    }
};
