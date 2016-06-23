# timeout

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordlist = []
        for i in words:
            letters = [0 for k in xrange(26)]
            for j in i:
                letters[ord(j) - ord('a')] = 1
            wordlist += [letters[:]]
        res = 0
        for i in xrange(len(wordlist)):
            for j in xrange(i+1, len(wordlist)):
                different = 0
                for k in xrange(len(wordlist[i])):
                    if wordlist[i][k] & wordlist[j][k] == 1:
                        break
                    else:
                        different += 1
                if different == 26:
                    res = max(res, len(words[i]) * len(words[j]))
        return res
