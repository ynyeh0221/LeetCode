class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.res = []
        used = [False for i in xrange(len(nums))]
        self.DFS([], used, nums)
        return self.res
        
    def DFS(self, path, used, nums):
        if len(path) == len(nums):
            self.res+=[path[:]]
            return
        for i in xrange(len(nums)):
            if not used[i]:
                if i>0 and not used[i-1] and nums[i] == nums[i-1]:
                    continue
                path += [nums[i]]
                used[i] = True
                self.DFS(path, used, nums)
                path.pop()
                used[i] = False
