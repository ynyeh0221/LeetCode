class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = 1
        res = 0
        for i in xrange(len(s)-1, -1, -1):
            res += (ord(s[i]) - ord('A') + 1) * base
            base *= 26
        return res
