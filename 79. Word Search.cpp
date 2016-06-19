// timeout

class Solution {
private:
    int m = 0;
    int n = 0;
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();
        vector <vector<bool>> visited (m, vector <bool> (n, false));
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (DFS(i, j, 0, board, word, visited)) return true;
            }
        }
        return false;
    }
    
    bool DFS(int i, int j, int windex, vector<vector<char>> board, string word, vector <vector<bool>> visited)
    {
        if (windex == word.size()) return true;
        if (i<0 || j<0 || i>=m || j>=n || visited[i][j] || board[i][j] != word[windex]) return false;
        visited[i][j] = true;
        bool res = DFS(i-1, j, windex+1, board, word, visited) || DFS(i+1, j, windex+1, board, word, visited) || DFS(i, j-1, windex+1, board, word, visited) || DFS(i, j+1, windex+1, board, word, visited);
        visited[i][j] = false;
        return res;
    }
};
