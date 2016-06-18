class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 12:
            return []
        self.res = []
        self.DFS(0, [], s)
        return self.res
        
    def DFS(self, start, path, s):
        if start > len(s):
            return
        if start == len(s):
            if len(path) == 4:
                self.res +=['.'.join(path)]
            return
        for j in xrange(1,4):
            if j > 1 and s[start] == '0':
                break
            temp = s[start:start+j]
            if int(temp) >= 0 and int(temp) <= 255:
                path = path + [temp]
                self.DFS(start+j, path, s)
                path.pop()
