class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        vector <vector<bool>> visited (board.size(), vector <bool> (board[0].size(), false));
        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {
                if (DFS(board, i, j, 0, word))
                    return true;
            }
        }
        return false;
    }
    
    bool DFS(vector<vector<char> > &board, int i, int j, int windex, string word)
     {
         if(board[i][j] == word[windex])
         {
             if(windex == word.size() - 1)
                 return true;
             board[i][j] = '*';
             if(i + 1 < board.size() && DFS(board, i + 1, j, windex + 1, word))
                 return true;
             if(i - 1 >= 0 && DFS(board, i - 1, j, windex + 1, word))
                 return true;
             if(j + 1 < board[0].size() && DFS(board, i, j + 1, windex + 1, word))
                 return true;
             if(j - 1 >= 0 && DFS(board, i, j - 1, windex + 1, word))
                 return true;
             board[i][j] = word[windex];
         }
         return false;
     }
};
