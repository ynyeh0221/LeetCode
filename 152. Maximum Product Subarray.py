class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [[0 for j in xrange(2)] for i in xrange(len(nums) + 1)]
        T[1][0], T[1][1], res = nums[0], nums[0], nums[0]
        for i in xrange(2, len(nums) + 1):
            T[i][0] = max(T[i-1][0] * nums[i-1], T[i-1][1] * nums[i-1], nums[i-1])
            T[i][1] = min(T[i-1][0] * nums[i-1], T[i-1][1] * nums[i-1], nums[i-1])
            res = max(T[i][0], res)
        return res
