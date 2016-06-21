// timeout

class Solution {
private:
    vector <string> res;
public:
    string getPermutation(int n, int k) {
        vector <bool> visited (n, false);
        DFS("", n, k, visited);
        return res[k-1];
    }
    
    void DFS(string path, int n, int k, vector <bool> visited)
    {
        if (path.length() == n)
        {
            res.push_back(path);
            return;
        }
        if (res.size() < k)
        {
            for (int i = 1; i <= n; i++)
            {
                if (!visited[i-1])
                {
                    visited[i-1] = true;
                    DFS(path + to_string(i), n, k, visited);
                    visited[i-1] = false;
                }
            }
        }
    }
};
