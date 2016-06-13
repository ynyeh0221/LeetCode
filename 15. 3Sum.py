class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        res = []
        
        i=0
        while i < n:
            j = i+1
            k = n-1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    res += [[nums[i], nums[j], nums[k]]]
                    j += 1
                    k -= 1
                    while j > 0 and j < n and nums[j] == nums[j-1]:
                        j += 1
                    while k > 0 and k < n-1 and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                    while k > 0 and k < n-1 and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                    while j > 0 and j < n and nums[j] == nums[j-1]:
                        j += 1
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
        return res
