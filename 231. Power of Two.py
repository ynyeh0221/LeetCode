class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return True if n>0 and int(math.log10(n)/math.log10(2)) == math.log10(n)/math.log10(2) else False
