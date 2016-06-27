class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        res = []
        for i in xrange(len(nums)-1, -1, -1):
            temp = [nums[i]]
            pre = nums[i]
            for j in xrange(i-1, -1, -1):
                if pre % nums[j] == 0:
                    temp += [nums[j]]
                    pre = nums[j]
            if len(res) < len(temp):
                res = temp
        return res[::-1]
