from fractions import gcd
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if z > x+y:
            return False
        return True if z % gcd(x,y) == 0 else False
