class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        ind2 = ind3 = ind5 = 0
        dic = {}
        while len(res) < n:
            minn = min(2*res[ind2], 3*res[ind3], 5*res[ind5])
            if minn == 2*res[ind2]:
                ind2 += 1
            elif minn == 3*res[ind3]:
                ind3 += 1
            else:
                ind5 += 1
            if minn not in dic:
                res += [minn]
                dic[minn] = 1
        return res[n-1]
