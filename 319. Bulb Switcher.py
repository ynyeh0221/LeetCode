class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in xrange(1, n+1):
            if i*i < n+1:
                res += 1
            else:
                break
        return res
