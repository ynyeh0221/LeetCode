class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m=len(matrix)
        if m>0:
            n=len(matrix[0])
            self.T=[[0 for j in xrange(n)] for i in xrange(m)]
            self.T[0][0]=matrix[0][0]
            for i in xrange(1,m):
                self.T[i][0]=self.T[i-1][0]+matrix[i][0]
            for j in xrange(1,n):
                self.T[0][j]=self.T[0][j-1]+matrix[0][j]
            for i in xrange(1,m):
                for j in xrange(1,n):
                    self.T[i][j]=matrix[i][j]+self.T[i][j-1]+self.T[i-1][j]-self.T[i-1][j-1]
            print self.T

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1==0 and col1==0:
            return self.T[row2][col2]
        elif row1>0 and col1==0:
            return self.T[row2][col2]-self.T[row1-1][col2]
        elif row1==0 and col1>0:
            return self.T[row2][col2]-self.T[row2][col1-1]
        return self.T[row2][col2]-self.T[row1-1][col2]-self.T[row2][col1-1]+self.T[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
