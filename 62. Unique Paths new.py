class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        T = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            T[i][0] = 1
        for j in xrange(n):
            T[0][j] = 1
        for i in xrange(1, m):
            for j in xrange(1, n):
                T[i][j] = T[i-1][j] + T[i][j-1]
        return T[m-1][n-1]
