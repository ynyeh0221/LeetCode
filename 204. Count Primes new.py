class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        T = [1 for i in xrange(n)]
        T[0], T[1] = 0, 0
        
        for i in xrange(2, n):
            if i*i < n:
                for j in xrange(i*i, n, i):
                    T[j] = 0
            else:
                break
        return sum(T)
