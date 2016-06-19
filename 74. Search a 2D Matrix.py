class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target >= row[0] and target <= row[len(row)-1]:
                return True if target in row else False
        return False
