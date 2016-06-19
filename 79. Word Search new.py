class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.DFS(i, j, 0, visited, board, word):
                    return True
        return False
    
    def DFS(self, i, j, windex, visited, board, word):
        if windex == len(word):
            return True    
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[windex]:
            return False
        visited[i][j] = True
        res = self.DFS(i-1, j, windex+1, visited, board, word) or self.DFS(i+1, j, windex+1, visited, board, word) or self.DFS(i, j-1, windex+1, visited, board, word) or self.DFS(i, j+1, windex+1, visited, board, word)
        visited[i][j] = False
        return res
