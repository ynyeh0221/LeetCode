class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if len(strs) == 0:
            return ""
        for j in xrange(len(strs[0])):
            for i in xrange(1, len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
        return res
