class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True
            dic[nums[i]] = i
        return False
