class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = r = 0
        res = len(nums) + 1
        while r < len(nums):
            if sum(nums[l:r+1]) < s:
                r += 1
            else:
                res = min(res, r+1-l)
                l += 1
        return res if res < len(nums) + 1 else 0
