class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = n
        for i in xrange(n):
            res ^= i
            res ^= nums[i]
        return res
