# timeout

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.combination(1, [], n, k)
        return self.res
    
    def combination(self, start, path, n, k):
        if len(path) == k:
            self.res += [path[:]]
            return
        for i in xrange(start, n+1):
            self.combination(i+1, path + [i], n, k)
