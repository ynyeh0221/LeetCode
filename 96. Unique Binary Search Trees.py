class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        T = [0 for i in xrange(n+1)]
        T[0], T[1] = 1, 1
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                T[i] += T[j-1] * T[i-j]
        return T[n]
