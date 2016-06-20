class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        T = [1 for i in xrange(len(nums))]
        res = 1
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    T[i] = max(T[i], T[j] + 1)
            res = max(res, T[i])
        return res
