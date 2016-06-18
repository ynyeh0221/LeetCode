class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = [[]]
        nums = sorted(nums)
        for k in xrange(1, len(nums)+1):
            self.combination(nums, [], 0, k)
        return self.res
    
    def combination(self, nums, path, start, k):
        if len(path) == k:
            self.res += [path[:]]
            return
        i = start
        while i<len(nums):
            self.combination(nums, path + [nums[i]], i+1, k)
            i += 1
            while i<len(nums) and nums[i] == nums[i-1]:
                i += 1
