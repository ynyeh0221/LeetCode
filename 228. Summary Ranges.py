class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) > 0:
            begin, end = nums[0], nums[0]
            for i in xrange(1, len(nums)):
                if nums[i] == end + 1:
                    end = nums[i]
                else:
                    if begin != end:
                        res += [str(begin) + "->" +str(end)]
                    else:
                        res += [str(begin)]
                    begin, end = nums[i], nums[i]
            if begin != end:
                res += [str(begin) + "->" +str(end)]
            else:
                res += [str(begin)]
        return res
