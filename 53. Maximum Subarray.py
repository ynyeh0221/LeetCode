import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [0 for i in xrange(len(nums) + 1)]
        T[0], res = -sys.maxint, -sys.maxint
        for i in xrange(1, len(nums)+1):
            T[i] = max(T[i-1]+nums[i-1], nums[i-1])
            res = max(res, T[i])
        return res
