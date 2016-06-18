class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]
        for k in xrange(1, len(nums)+1):
            self.combination(nums, [], 0, k)
        return self.res
    
    def combination(self, nums, path, start, k):
        if len(path) == k:
            self.res += [path[:]]
            return
        for i in xrange(start, len(nums)):
            self.combination(nums, path + [nums[i]], i+1, k)
