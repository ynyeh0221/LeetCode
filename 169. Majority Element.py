class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        majority_l = self.majorityElement(nums[:len(nums)/2])
        majority_r = self.majorityElement(nums[len(nums)/2:])
        temp_l = 0
        temp_r = 0
        for i in nums:
            if i == majority_l:
                temp_l += 1
            if i == majority_r:
                temp_r += 1
        if temp_l > len(nums)/2:
            return majority_l
        if temp_r > len(nums)/2:
            return majority_r
