class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n == 4:
            return 4
        elif n == 5:
            return 6
        elif n == 6:
            return 9
        T = [0 for i in xrange(n+1)]
        T[4] = 4
        T[5] = 6
        T[6] = 9
        for i in xrange(7, n+1):
            T[i] = T[i-3] * 3
        return T[n]
