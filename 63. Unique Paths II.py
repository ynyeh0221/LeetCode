class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        T = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            if obstacleGrid[i][0] == 0:
                T[i][0] = 1
            else:
                break
        for j in xrange(n):
            if obstacleGrid[0][j] == 0:
                T[0][j] = 1
            else:
                break
        for i in xrange(1, m):
            for j in xrange(1, n):
                if obstacleGrid[i][j] == 0:
                    T[i][j] = T[i-1][j] + T[i][j-1]
        return T[m-1][n-1]
