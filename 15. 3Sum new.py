class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        res = set()
        dic={}
        
        for i in xrange(n):
            if nums[i] not in dic:
                dic[nums[i]] = i
        for i in xrange(n):
            for j in xrange(i+1,n):
                if -(nums[i] + nums[j]) in dic and dic[-(nums[i] + nums[j])] != i and dic[-(nums[i] + nums[j])] != j:
                    temp = tuple( sorted( [nums[i], nums[j], nums[dic[-(nums[i]+nums[j])]]] ))
                    res.add(temp)
        return list(res)
