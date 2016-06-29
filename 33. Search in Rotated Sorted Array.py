class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        temp = nums[0]
        if target == temp:
            return 0
        elif target > temp:
            for i in xrange(len(nums)):
                if nums[i] < temp:
                    return -1
                if nums[i] == target:
                    return i
            return -1
        else:
            for i in xrange(len(nums)-1, -1, -1):
                if nums[i] >= temp:
                    return -1
                if nums[i] == target:
                    return i
            return -1
