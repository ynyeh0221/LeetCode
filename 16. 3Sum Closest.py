import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        nums = sorted(nums)
        res = 0
        difference = sys.maxint
        i=0
        while i < n:
            j = i+1
            k = n-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == target:
                    return target
                elif temp > target:
                    k -= 1
                    while k > 0 and k < n-1 and nums[k] == nums[k+1]:
                        k -= 1
                    if abs(temp-target) < difference:
                        res=temp
                        difference = abs(temp-target)
                else:
                    j += 1
                    while j > 0 and j < n and nums[j] == nums[j-1]:
                        j += 1
                    if abs(temp-target) < difference:
                        res=temp
                        difference = abs(temp-target)
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
        return res
