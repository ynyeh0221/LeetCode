# timeout

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        T = [1 for i in xrange(n)]
        T[0] = 0
        T[1] = 0
        
        for j in xrange(2, n):
            if j*j <= n:
                for i in xrange(j+1, n):
                    if i % j == 0:
                        T[i] = 0
            else:
                break
        return sum(T)
