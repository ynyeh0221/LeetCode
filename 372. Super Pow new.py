class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1337
        b = int(''.join(str(j) for j in b))
        res = 1
        a = a % mod
        while b > 0:
            if b % 2 == 1:
                res = (res * a) % mod
            b = b/2
            a = (a * a) % mod
        return res
