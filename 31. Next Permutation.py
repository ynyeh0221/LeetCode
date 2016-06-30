import sys
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ind1, ind2 = len(nums)-1, len(nums)-1
        for i in xrange(len(nums)-1, -1, -1):
            if nums[i] > nums[i-1]:
                ind1 = i - 1
                break
        minn = sys.maxint
        for j in xrange(ind1+1, len(nums)):
            if nums[j] < minn and nums[j] > nums[ind1]:
                minn = nums[j]
                ind2 = j
        nums[ind1], nums[ind2] = nums[ind2], nums[ind1]
        temp = sorted(nums[ind1+1:])
        for i in xrange(ind1+1, len(nums)):
            nums[i] = temp[i-ind1-1]
