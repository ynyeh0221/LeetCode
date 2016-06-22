class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank = [gas[i] - cost[i] for i in xrange(len(gas))] # current gas in tank
        if sum(tank) < 0:
            return -1
        i = 0
        while i < len(tank):
            if tank[i] < 0: # only tank[i] >= 0 can be start point
                i += 1
            temp = 0
            for j in xrange(i, len(tank)):
                if temp < 0:
                    break
                temp += tank[j]
            for j in xrange(i):
                if temp < 0:
                    break
                temp += tank[j]
            if temp >= 0:
                return i
            i += 1
        return -1
