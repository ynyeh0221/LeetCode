from collections import defaultdict
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        dic = defaultdict(set)
        res = set()
        
        for i in xrange(n):
            for j in xrange(i+1, n):
                for pair in dic[target - (nums[i] + nums[j])]:
                    res.add(tuple( list(pair) + [nums[i], nums[j]] ))
            for j in xrange(i):
                dic[nums[i] + nums[j]].add((nums[j], nums[i]))
        return list(res)
