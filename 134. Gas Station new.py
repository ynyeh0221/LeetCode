class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        i = start = sum = totalsum = 0
        while i < len(gas):
            sum += gas[i] - cost[i]
            totalsum += gas[i] - cost[i]
            if sum < 0:
                sum = 0
                start = i + 1
            i += 1
        return -1 if totalsum < 0 else start
