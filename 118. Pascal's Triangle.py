class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        res = [[1], [1, 1]]
        for i in xrange(3, numRows + 1):
            temp = [1]
            for j in xrange(1, len(res[i-2])):
                temp += [res[i-2][j-1] + res[i-2][j]]
            temp += [1]
            res += [temp[:]]
        return res
