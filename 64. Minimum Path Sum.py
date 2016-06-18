class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        T = [[0 for j in xrange(n + 1)] for i in xrange(m + 1)]
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if i == 1:
                    T[1][j] = T[1][j-1] + grid[0][j-1]
                elif j == 1:
                    T[i][1] = T[i-1][1] + grid[i-1][0]
                else:
                    T[i][j] = min(T[i-1][j], T[i][j-1]) + grid[i-1][j-1]
        return T[m][n]
