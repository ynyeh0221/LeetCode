class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        dicA = {}
        dic = {}
        numB = 0
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                dicA[i] = 1
            else:
                if secret[i] not in dic:
                    dic[secret[i]] = 0
                dic[secret[i]] += 1
        for i in xrange(len(guess)):
            if guess[i] in dic and i not in dicA:
                if dic[guess[i]] > 0:
                    numB += 1
                    dic[guess[i]] -= 1
        return str(len(dicA)) + 'A' + str(numB) + 'B'
