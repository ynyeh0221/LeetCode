import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        candidates = [1 for i in xrange(len(primes))]  
        inds = [0 for i in xrange(len(primes))] 
        res = [1]  
        minn = 1  
        while len(res) < n:  
            for i in range(len(primes)):  
                if minn == candidates[i] :  
                    candidates[i] = res[inds[i]] * primes[i]  
                    inds[i] += 1  
            minn = min(candidates)  
            res.append(minn)  
        return res[-1] 
