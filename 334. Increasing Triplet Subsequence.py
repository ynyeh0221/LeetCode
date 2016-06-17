import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x1, x2 = sys.maxint, sys.maxint
        for i in nums:
            if i < x1:
                x1 = i
            elif i > x1 and i < x2:
                x2 = i
            elif i > x2:
                return True
        return False
