# timeout

import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        inds = [0 for i in xrange(len(primes))]
        res = [1]
        dic = {}
        while len(res) < n:
            minn = sys.maxint
            index = 0
            for i in xrange(len(primes)):
                temp = primes[i]*res[inds[i]]
                if temp < minn:
                    minn = temp
                    index = i
            inds[index] += 1
            if minn not in dic:
                res += [minn]
                dic[minn] = 1
        return res[n-1]
