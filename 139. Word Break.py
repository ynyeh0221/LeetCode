class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        T = [False for i in xrange(len(s)+1)]
        T[0] = True
        for i in xrange(1, len(s)+1):
            for j in xrange(i):
                if T[j] and s[j:i] in wordDict:
                    T[i] = True
        return T[len(s)]
