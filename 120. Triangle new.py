class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        T = [[0 for j in xrange(len(triangle[i]))] for i in xrange(len(triangle))]
        T[0][0] = triangle[0][0]
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])):
                if j > 0 and j < len(triangle[i-1]):
                    T[i][j] = min(T[i - 1][j] + triangle[i][j], T[i - 1][j - 1] + triangle[i][j])
                else:
                    if j == 0:
                        T[i][j] = T[i - 1][j] + triangle[i][j]
                    if j == len(triangle[i-1]):
                        T[i][j] = T[i - 1][j - 1] + triangle[i][j]
        return min(T[len(triangle) - 1])
