def compare(a, b):
    if int(a+b) > int(b+a):
        return 1
    elif int(a+b) < int(b+a):
        return -1
    else:
        return 0
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = map(str, nums)
        nums = sorted(nums, cmp = compare, reverse = True)
        return '0' if nums[0] == '0' else ''.join(nums)
