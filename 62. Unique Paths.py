class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        res = 1
        for i in xrange(m, m+n-1):
            res *= i
        for i in xrange(1, n):
            res /= i
        return res
