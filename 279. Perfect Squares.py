# timeout

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [n+1 for i in xrange(n+1)]
        for i in xrange(1, n + 1):
            if i*i <= n:
                T[i*i] = 1
        for i in xrange(1, n + 1):
            for j in xrange(1, i):
                T[i] = min(T[i], T[i-j] + T[j])
        return T[n]
