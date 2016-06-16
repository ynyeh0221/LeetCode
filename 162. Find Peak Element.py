class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        elif nums[len(nums)-2] < nums[len(nums)-1]:
            return len(nums)-1
        else:
            for i in xrange(1, len(nums)-1):
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
