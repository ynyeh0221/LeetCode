class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minn = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < minn:
                return nums[i]
        return minn
