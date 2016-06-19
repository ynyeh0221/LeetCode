class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.DFS(n, n, n, "")
        return self.res
        
    def DFS(self, left, right, n, path):
        if len(path) == 2*n:
            self.res += [path]
            return
        if left == right:
            self.DFS(left-1, right, n, path + '(')
        elif left < right:
            for i in xrange(2):
                if i == 0:
                    self.DFS(left, right-1, n, path + ')')
                else:
                    if left > 0:
                        self.DFS(left-1, right, n, path + '(')
