# timeout

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in xrange(len(nums)):
            for j in xrange(1, k+1):
                if i+j < len(nums) and abs(nums[i+j] - nums[i]) <= t:
                    return True
        return False
