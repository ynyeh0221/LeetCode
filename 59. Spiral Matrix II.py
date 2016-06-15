class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.n = n
        matrix = [[n**2 for j in xrange(n)] for i in xrange(n)]
        self.current_n = 1
        self.DFS(matrix, 0, 0, 0, n-1, 1, n-1, "R")
        return matrix
        
    def DFS(self, matrix, i, j, xmin, xmax, ymin, ymax, direction):
        if self.current_n >= self.n**2:
            return
        if direction == "R":
            while j < xmax:
                matrix[i][j] = self.current_n
                j += 1
                self.current_n += 1
            self.DFS(matrix, i, j, xmin, xmax-1, ymin, ymax, "D")
        elif direction == "D":
            while i < ymax:
                matrix[i][j] = self.current_n
                i += 1
                self.current_n += 1
            self.DFS(matrix, i, j, xmin, xmax, ymin, ymax-1, "L")
        elif direction == "L":
            while j > xmin:
                matrix[i][j] = self.current_n
                j -= 1
                self.current_n += 1
            self.DFS(matrix, i, j, xmin+1, xmax, ymin, ymax, "U")
        elif direction == "U":
            while i > ymin:
                matrix[i][j] = self.current_n
                i -= 1
                self.current_n += 1
            self.DFS(matrix, i, j, xmin, xmax, ymin+1, ymax, "R")
