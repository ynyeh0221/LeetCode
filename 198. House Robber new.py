class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [0 for i in xrange(len(nums) + 1)]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 or len(nums) == 2:
            return max(nums)
            
        T[1] = nums[0]
        for i in xrange(2, len(nums) + 1):
            T[i] = max(T[i - 1], T[i - 2] + nums[i - 1])
        return T[len(nums)]
