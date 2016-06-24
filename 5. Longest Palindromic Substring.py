# timeout

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = s[0]
        T = [[False for j in xrange(len(s))] for i in xrange(len(s))]
        for i in xrange(len(s)):
            for j in xrange(i):
                T[j][i] = (s[j] == s[i] and (i-j < 2 or T[j+1][i-1]))
                if T[j][i]:
                    if i-j+1 > len(res):
                        res = s[j:i+1]
            T[i][i] = 1
        return res
