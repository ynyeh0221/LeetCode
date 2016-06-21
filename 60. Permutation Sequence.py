# timeout

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.res = []
        visited = [False for i in xrange(n)]
        self.DFS("", n, k, visited)
        return self.res[k-1]
        
    def DFS(self, path, n, k, visited):
        if len(path) == n:
            self.res += [path]
            return
        if len(self.res) < k:
            for i in xrange(1, n+1):
                if visited[i-1] == False:
                    visited[i-1] = True
                    self.DFS(path + str(i), n, k, visited)
                    visited[i-1] = False
