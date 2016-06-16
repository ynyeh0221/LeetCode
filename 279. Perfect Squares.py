# timeout

import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [n+1 for i in xrange(n+1)]
        for i in xrange(1, n + 1):
            if int(math.sqrt(i))**2 == i:
                T[i] = 1
            else:
                for j in xrange(1, i + 1):
                    T[i] = min(T[i], T[i-j] + T[j])
        return T[n]
