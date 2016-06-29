class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        temp = nums[0]
        if target == temp:
            return True
        elif target > temp:
            for i in xrange(len(nums)):
                if nums[i] < temp:
                    return False
                if nums[i] == target:
                    return True
            return False
        else:
            for i in xrange(len(nums)-1, -1, -1):
                if nums[i] > temp:
                    return False
                if nums[i] == target:
                    return True
            return False
