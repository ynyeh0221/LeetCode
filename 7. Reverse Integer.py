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
        temp = int(str(x)[::-1])
        if temp >= 2147483647:
            return 0
        return temp if sign == 1 else -temp
