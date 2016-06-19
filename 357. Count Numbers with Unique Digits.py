class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        for i in xrange(1,n):
            temp = 9
            for j in xrange(9, 9 - i, -1):
                temp *= j
            res += temp
        return res
