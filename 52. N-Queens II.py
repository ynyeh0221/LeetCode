class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        self.DFS([], n)
        return self.res
        
    def check(self, path, i):
        for j in xrange(len(path)):
            if i == path[j] or len(path)-j == abs(path[j] - i):
                return False
        return True
    def DFS(self, path, n):
        if len(path) == n:
            self.res += 1
        for i in xrange(n):
            if self.check(path, i):
                self.DFS(path + [i], n)
