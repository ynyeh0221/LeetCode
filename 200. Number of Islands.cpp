class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0) return 0;
        vector <vector<bool>> visited (grid.size(), vector<bool> (grid[0].size(), false));
        int num_of_island = 0;
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (grid[i][j] == '1' && visited[i][j] == false)
                {
                    num_of_island ++;
                    DFS(i, j, grid, visited);
                }
            }
        }
        return num_of_island;
    }
    
    void DFS(int i, int j, vector<vector<char>>& grid, vector <vector<bool>>& visited)
    {
        visited[i][j] = true;
        if (i-1 >=0 && grid[i-1][j] == '1' && visited[i-1][j] == false)
            DFS(i-1, j, grid, visited);
        if (i+1 < grid.size() && grid[i+1][j] == '1' && visited[i+1][j] == false)
            DFS(i+1, j, grid, visited);
        if (j-1 >= 0 && grid[i][j-1] == '1' && visited[i][j-1] == false)
            DFS(i, j-1, grid, visited);
        if (j+1 < grid[0].size() && grid[i][j+1] == '1' && visited[i][j+1] == false)
            DFS(i, j+1, grid, visited);
        return;
    }
};
