class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq1 = [0 for i in xrange(26)]
        freq2 = [0 for i in xrange(26)]
        for i, j in zip(s, t):
            freq1[ord(i) - ord('a')] += 1
            freq2[ord(j) - ord('a')] += 1
        return True if freq1 == freq2 else False
