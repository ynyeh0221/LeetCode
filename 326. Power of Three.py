import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n>0 and int(math.log10(n)/math.log10(3)) == math.log10(n)/math.log10(3) else False
