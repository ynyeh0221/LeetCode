class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            try:
                return self.power(x, n)
            except OverflowError:
                return float(0)
        else:
            n = -n
            try:
                return float(1 / self.power(x, n))
            except OverflowError:
                return float(0)
        
    def power(self, x, n):
        if n == 0:
            return float(1)
        elif n == 1:
            return float(x)
        return float(self.power(x, n/2)**2 * self.power(x, n%2))
