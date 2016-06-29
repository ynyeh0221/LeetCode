class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        i = 0
        while i < len(nums):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            dic[nums[i]] += 1
            if dic[nums[i]] >= 3:
                nums.pop(i)
                i -= 1
            i += 1
        return len(nums)
