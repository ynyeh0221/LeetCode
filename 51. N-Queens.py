class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        self.DFS([], n)
        return self.res
        
    def check(self, path, i):
        for j in xrange(len(path)):
            if i == path[j] or len(path)-j == abs(path[j] - i):
                return False
        return True
    def DFS(self, path, n):
        if len(path) == n:
            temp=[]
            for i in xrange(len(path)):
                row=""
                for j in xrange(n):
                   if j!=path[i]:
                       row+="."
                   else:
                       row+="Q"
                temp+=[row]
            self.res+=[temp[:]]
        for i in xrange(n):
            if self.check(path, i):
                self.DFS(path + [i], n)
