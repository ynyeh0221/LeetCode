class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        T = [0 for i in xrange(len(nums))]
        T[0] = nums[0]
        if len(nums) > 1 and T[0] < 1:
            return False
        for i in xrange(1, len(nums)):
            T[i] = max(T[i-1], nums[i] + i)
            if len(nums) > i+1 and T[i] < i+1:
                return False
        return True
