# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        
        while start <= end:
            mid = (start + end)/2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid - 1
        return start
