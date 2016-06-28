class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0
        for i in xrange(len(haystack)):
            if i + len(needle) <= len(haystack) and haystack[i:i + len(needle)] == needle:
                return i
        return -1
