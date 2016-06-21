class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        DFS({}, 0, candidates, target);
        return res;
    }
    
    void DFS(vector <int> path, int start, vector<int>& candidates, int target)
    {
        if (target == 0)
        {
            res.push_back(path);
            return;
        }
        int i = start;
        while (i < candidates.size())
        {
            if (candidates[i] <= target)
            {
                path.push_back(candidates[i]);
                DFS(path, i + 1, candidates, target - candidates[i]);
                path.pop_back();
            }
            i++;
            while (i < candidates.size() && candidates[i] == candidates[i-1])
                i++;
        }
    }
};
