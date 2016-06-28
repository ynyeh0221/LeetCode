class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bin_m = bin(m)[2:]
        bin_n = bin(n)[2:]
        for i in xrange(len(bin_n) - len(bin_m)):
            bin_n = '0' + bin_n
        res = 0
        for i in xrange(len(bin_n), -1, -1):
            if bin_m[:i] == bin_n[:i]:
                for j in xrange(i-1, -1, -1):
                    res += int(bin_m[j]) * pow(2, len(bin_m) - 1 - j)
                break
        return res
