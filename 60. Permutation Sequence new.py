import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums =  [i for i in xrange(1, n+1)]
        k -= 1
        res = ""
        while n > 0:
            temp = math.factorial(n-1)
            res += str(nums[k / temp])
            nums.pop(k / temp)
            k %= temp
            n -= 1
        return res
