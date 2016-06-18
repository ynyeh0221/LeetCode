class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        T = [0 for i in xrange(len(nums))]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1 or len(nums) == 2:
            return max(nums)
            
        T[0], T[1] = nums[0], nums[1]
        for i in xrange(2, len(nums)):
            for j in xrange(i-1):
                T[i] = max(T[i], T[i-1], T[j] + nums[i])
        return T[len(nums) - 1]
