class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        pre = [1, 1]
        for i in xrange(2, rowIndex + 1):
            temp = [1]
            for j in xrange(1, len(pre)):
                temp += [pre[j-1] + pre[j]]
            temp += [1]
            pre = temp[:]
        return pre
