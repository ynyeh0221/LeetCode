class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        self.visited = [[False for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        num_of_island = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == '1' and self.visited[i][j] == False:
                    num_of_island += 1
                    self.DFS(i, j, grid)
        return num_of_island
        
    def DFS(self, i, j, grid):
        self.visited[i][j] = True
        if i-1 >= 0 and grid[i-1][j] == '1' and self.visited[i-1][j] == False:
            self.DFS(i-1, j, grid)
        if i+1 < len(grid) and grid[i+1][j] == '1' and self.visited[i+1][j] == False:
            self.DFS(i+1, j, grid)
        if j-1 >= 0 and grid[i][j-1] == '1' and self.visited[i][j-1] == False:
            self.DFS(i, j-1, grid)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1' and self.visited[i][j+1] == False:
            self.DFS(i, j+1, grid)
        return
