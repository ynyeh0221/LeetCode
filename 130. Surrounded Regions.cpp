class Solution {
public:
    void solve(vector<vector<char>>& board) {
        if (board.size() == 0 || board[0].size() == 0) return;
        for (int i = 0; i < board.size(); i++)
        {
            DFS(i, 0, board);
            DFS(i, board[0].size()-1, board);
        }
        for (int j = 0; j < board[0].size(); j++)
        {
            DFS(0, j, board);
            DFS(board.size()-1, j, board);
        }
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '*') board[i][j] = 'O';
            }
        }
    }
    void DFS(int i, int j, vector<vector<char>>& board)
    {
        queue <int> qx, qy;
        qx.push(i);
        qy.push(j);
        while (!qx.empty())
        {
            int x = qx.front();
            qx.pop();
            int y = qy.front();
            qy.pop();
            if (x < 0 || y < 0 || x >= board.size() || y >= board[0].size() || board[x][y] != 'O')
                continue;
            board[x][y] = '*';
            qx.push(x-1); qy.push(y);
            qx.push(x+1); qy.push(y);
            qx.push(x); qy.push(y-1);
            qx.push(x); qy.push(y+1);
        }
    }
};
