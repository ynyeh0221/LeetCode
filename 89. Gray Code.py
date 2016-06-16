class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in xrange(n):
            temp = []
            for j in xrange(len(res)):
                temp += [res[j]]
            for j in xrange(len(res)-1, -1, -1):
                temp += [res[j] + 2**i]
            res[:] = temp[:]
        return res
