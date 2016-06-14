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
            for c in coins:
                if c <= a:
                    T[a] = min(T[a - c] + 1, T[a])
        return T[amount] if T[amount] != amount + 1 else -1
