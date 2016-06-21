class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates = sorted(candidates)
        self.DFS([], 0, candidates, target)
        return self.res
        
    def DFS(self, path, start, candidates, target):
        if target == 0:
            self.res += [path]
            return
        i = start
        while i < len(candidates):
            if candidates[i] <= target:
                self.DFS(path + [candidates[i]], i+1, candidates, target - candidates[i])
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
