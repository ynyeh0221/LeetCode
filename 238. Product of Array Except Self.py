class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1 for i in xrange(len(nums))]
        temp = 1
        for i in xrange(1, len(nums)):
            temp *= nums[i-1]
            res[i] *= temp
        temp = 1
        for i in xrange(len(nums)-1, -1, -1):
            if i<len(nums)-1:
                temp *= nums[i+1]
            res[i] *= temp
        return res
