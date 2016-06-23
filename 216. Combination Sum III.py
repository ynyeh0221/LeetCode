class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS([], 1, k, n)
        return self.res
        
    def DFS(self, path, start, k, n):
        if len(path) == k or n == 0 or start == 10:
            if len(path) == k and n == 0:
                self.res += [path[:]]
            return
        for i in xrange(start, 10):
            if i <= n:
                self.DFS(path + [i], i+1, k, n-i)
