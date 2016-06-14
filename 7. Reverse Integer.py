class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            x = -x
            sign = -1
        if int(str(x)[::-1]) >= 2147483647:
            return 0
        return int(str(x)[::-1]) if sign == 1 else -int(str(x)[::-1])
