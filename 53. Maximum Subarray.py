class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [0 for i in xrange(len(nums) + 1)]
        T[1], res = nums[0], nums[0]
        for i in xrange(2, len(nums)+1):
            T[i] = max(T[i-1]+nums[i-1], nums[i-1])
            res = max(res, T[i])
        return res
