# ref: http://bookshadow.com/weblog/2015/09/09/leetcode-perfect-squares/

class Solution(object):
    _T = [0]
    def numSquares(self, n):
        T = self._T
        while len(T) <= n:
            T += min(T[-i*i] for i in range(1, int(len(T)**0.5+1))) + 1,
        return T[n]
