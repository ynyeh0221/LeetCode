class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)[2:][::-1]
        while len(bin_n) < 32:
            bin_n += "0"
        return int(bin_n,2)
