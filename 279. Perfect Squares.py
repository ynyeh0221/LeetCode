# timeout

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [n+1 for i in xrange(n+1)]
        T[0], T[1]  = 0, 1
        for i in xrange(1, n + 1):
            for j in xrange(1, i):
                if j*j <= i:
                    T[i] = min(T[i], T[i-j*j] + 1)
        return T[n]
