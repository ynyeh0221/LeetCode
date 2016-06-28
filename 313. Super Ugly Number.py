# timeout

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
            temps = [primes[i]*res[inds[i]] for i in xrange(len(primes))]
            minn = min(temps)
            inds[temps.index(minn)] += 1
            if minn not in dic:
                res += [minn]
                dic[minn] = 1
        return res[n-1]
