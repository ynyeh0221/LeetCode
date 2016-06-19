import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        maxx = -sys.maxint
        start = prices[0]
        end = 0
        for i in range(1, len(prices)):
            end = prices[i]
            maxx = max(maxx, end - start)
            start = min(start, end)
        return 0 if maxx < 0 else maxx
