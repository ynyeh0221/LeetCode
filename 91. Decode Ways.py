# DFS, timeout

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s:
            self.res = 0
            self.DFS(0, s)
            return self.res
        return 0
        
    def DFS(self, i, s):
        if i == len(s):
            self.res += 1
            return
        for j in xrange(2):
            if j == 0:
                if s[i] != '0':
                    self.DFS(i+1, s)
                else:
                    return
            else:
                if s[i] != '0' and i+2 <= len(s) and int(s[i:i+2]) <= 26:
                    self.DFS(i+2, s)
                else:
                    return
