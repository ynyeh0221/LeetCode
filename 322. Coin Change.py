# timeout

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        T=[amount+1 for i in xrange(amount+1)]
        T[0] = 0
        for a in xrange(1, amount+1):
            for c in xrange(len(coins)):
                if coins[c]<=a:
                    T[a] = min(T[a - coins[c]] + 1, T[a])
        if T[amount] == amount+1:
            return -1
        return T[amount]
