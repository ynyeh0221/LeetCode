class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
        for i in xrange(len(nums)):
            if target - nums[i] in dic and i > dic[target-nums[i]]:
                return [dic[target-nums[i]], i]
