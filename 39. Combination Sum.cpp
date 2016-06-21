class Solution {
private:
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        DFS({}, candidates, target);
        return res;
    }
    
    void DFS(vector <int> path, vector<int>& candidates, int target)
    {
        if (target == 0)
        {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < candidates.size(); i++)
        {
            if (candidates[i] <= target)
            {
                if (path.size() > 0 && candidates[i] < path[path.size() - 1])
                    continue;
                path.push_back(candidates[i]);
                DFS(path, candidates, target - candidates[i]);
                path.pop_back();
            }
        }
    }
};
