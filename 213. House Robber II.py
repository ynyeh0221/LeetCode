class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        T0 = [0 for i in xrange(n + 1)]
        T1 = [0 for i in xrange(n + 1)]
        T0[1], T1[2] = nums[0], nums[1]
        for i in xrange(2, n):
            T0[i] = max(T0[i-1], T0[i-2] + nums[i-1])
        for i in xrange(3, n+1):
            T1[i] = max(T1[i-1], T1[i-2] + nums[i-1])
        return max(T0[n-1], T1[n])
