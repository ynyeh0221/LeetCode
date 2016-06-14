class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return True if num>0 and int(math.log10(num)/math.log10(4)) == math.log10(num)/math.log10(4) else False
