class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i in xrange(len(s) - 9):
            if s[i:i+10] in dic:
                dic[s[i:i+10]] += 1
                if dic[s[i:i+10]] == 2:
                    res += [s[i:i+10]]
            else:
                dic[s[i:i+10]] = 1
        return res
