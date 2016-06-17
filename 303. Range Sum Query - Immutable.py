class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.totalnums = nums
        for i in xrange(1, len(self.totalnums)):
            self.totalnums[i] += self.totalnums[i - 1]
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.totalnums[j]
        return self.totalnums[j] - self.totalnums[i - 1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
