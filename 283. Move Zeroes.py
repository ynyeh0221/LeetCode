class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        length = len(nums)
        while i < length:
            if nums[i] == 0:
                length -= 1
                nums.pop(i)
                nums.append(0)
            else:
                i += 1
