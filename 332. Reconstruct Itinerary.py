class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        fromto = {}
        visited = {}
        self.n = len(tickets)
        for i in tickets:
            if i[0] not in fromto:
                fromto[i[0]] = []
                visited[i[0]] = []
            fromto[i[0]] += [i[1]]
            visited[i[0]] += [False]
        for key in fromto.keys():
            fromto[key] = sorted(fromto[key]) # to make sure that the first solution has the smallest lexical order
        self.res = []
        self.DFS(["JFK"], "JFK", fromto, visited)
        return self.res
    
    def DFS(self, path, start, fromto, visited):
        if len(path) == self.n + 1:
            self.res = path[:]
            return
        try:
            for i in xrange(len(fromto[start])):
                if visited[start][i] == False:
                    visited[start][i] = True
                    self.DFS(path + [fromto[start][i]], fromto[start][i], fromto, visited)
                    visited[start][i] = False
                    if len(self.res) > 0: # If we have a solution, it must be the one with the smallest lexical order. So we don't need to find other solutions.
                        break
        except:
            return
