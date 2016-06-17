class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 1
        for i in xrange(m, m+n-1):
            res *= i
        for i in xrange(1, n):
            res /= i
        return res
