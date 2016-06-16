class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [0 for i in xrange(n + 1)]
        if n >= 1:
            T[1] = 1
        if n >= 2:
            T[2] = 2
        for i in xrange(3, n+1):
            T[i] = T[i-1] + T[i-2]
        return T[n]
