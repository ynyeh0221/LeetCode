class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        allnums = [i for i in xrange(len(nums)+1)]
        res = allnums[0]
        for i in xrange(1,len(allnums)):
            res ^= allnums[i]
        for i in xrange(len(nums)):
            res ^= nums[i]
        return res
