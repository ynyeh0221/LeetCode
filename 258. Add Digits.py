class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        numlist = map(int, str(num))
        while len(numlist) > 1:
            numlist = map(int, str(sum(numlist)))
        return numlist[0]
