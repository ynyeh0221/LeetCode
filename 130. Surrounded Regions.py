class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])
        for i in xrange(m):
            self.DFS(i, 0, board)
            self.DFS(i, n-1, board)
        for j in xrange(n):
            self.DFS(0, j, board)
            self.DFS(m-1, j, board)
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = "O"
    
    def DFS(self, i, j, board):
        m = len(board)
        n = len(board[0])
        queue = [(i,j)]
        while queue:
            (x, y) = queue.pop(0)
            if x < 0 or y < 0 or x >= m or y >= n or board[x][y] != 'O':
                continue
            board[x][y] = '*'
            queue += [(x-1, y)]
            queue += [(x+1, y)]
            queue += [(x, y-1)]
            queue += [(x, y+1)]
