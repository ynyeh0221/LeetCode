class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in xrange(len(nums)):
            if nums[i] == target:
                return i
            else:
                if target < nums[0]:
                    return 0
                elif target > nums[len(nums) - 1]:
                    return len(nums)
                else:
                    if i > 0 and nums[i-1] < target and nums[i] > target:
                        return i
