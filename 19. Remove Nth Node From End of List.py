class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        if nums[0] == target:
            res += [0]
        for i in xrange(1, len(nums)):
            if len(res) == 2:
                break
            if nums[i] == target and nums[i-1] != target:
                res += [i]
            elif nums[i] != target and nums[i-1] == target:
                res += [i-1]
        if len(res) == 1:
            res += [len(nums)-1]
        return res if len(res) > 0 and res[0] > -1 else [-1, -1]
