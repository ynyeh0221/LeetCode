class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS([], candidates, target)
        return list(self.res)
    
    def DFS(self, path, candidates, target):
        if target == 0:
            self.res += [path]
            return
        for i in candidates:
            if i <= target:
                if len(path) == 0:
                    self.DFS(path + [i], candidates, target - i)
                elif i >= path[len(path) - 1]:
                    self.DFS(path + [i], candidates, target - i)
