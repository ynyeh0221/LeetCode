class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordlist = []
        for i in words:
            letters = 0
            for j in i:
                letters|= 1 << ord(j) - ord('a')
            wordlist += [letters]
        res = 0
        for i in xrange(len(wordlist)):
            for j in xrange(i+1, len(wordlist)):
                if wordlist[i] & wordlist[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
