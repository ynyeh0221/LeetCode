# timeout

import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.res = sys.maxint
        self.DFS(triangle, [], 0, 0)
        return self.res
    
    def DFS(self, triangle, path, location, level):
        if len(path) == len(triangle):
            temp = sum(path)
            if temp < self.res:
                self.res = temp 
            return
        if location < len(triangle[level]):
            path += [triangle[level][location]]
            self.DFS(triangle, path, location, level+1)
            path.pop()
        if location + 1 < len(triangle[level]):
            path += [triangle[level][location + 1]]
            self.DFS(triangle, path, location + 1, level+1)
            path.pop()
