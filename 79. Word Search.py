# timeout

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.res = False
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    self.DFS(i, j, [board[i][j]], 1, visited, board, word)
                    visited[i][j] = False
                    if self.res == True:
                        return self.res
        return False
    
    def DFS(self, i, j, path, windex, visited, board, word):
        if windex == len(word):
            if "".join(path) == word :
                self.res = True    
            return
        if i-1 >= 0:
            if visited[i-1][j] == False and board[i-1][j] == word[windex]:
                visited[i-1][j] = True
                self.DFS(i-1, j, path + [board[i-1][j]], windex+1, visited, board, word)
                visited[i-1][j] = False
        if i+1 < len(board):
            if visited[i+1][j] == False and board[i+1][j] == word[windex]:
                visited[i+1][j] = True
                self.DFS(i+1, j, path + [board[i+1][j]], windex+1, visited, board, word)
                visited[i+1][j] = False
        if j-1 >= 0:
            if visited[i][j-1] == False and board[i][j-1] == word[windex]:
                visited[i][j-1] = True
                self.DFS(i, j-1, path + [board[i][j-1]], windex+1, visited, board, word)
                visited[i][j-1] = False
        if j+1 < len(board[0]):
            if visited[i][j+1] == False and board[i][j+1] == word[windex]:
                visited[i][j+1] = True
                self.DFS(i, j+1, path + [board[i][j+1]], windex+1, visited, board, word)
                visited[i][j+1] = False
