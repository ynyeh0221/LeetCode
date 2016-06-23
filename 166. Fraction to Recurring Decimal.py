class Solution(object):
    def fractionToDecimal(self, n, d):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if n == 0:
            return str(0)
        flag = 1 # deal with negative n and d
        if n < 0:
            n = -n
            flag *= -1
        if d < 0:
            d = -d
            flag *= -1
        if n % d == 0:
            return str(n / d) if flag == 1 else '-' + str(n / d)
        res = str(n / d) + "."
        dic = {}
        n = (n % d) * 10
        while n > 0:
            if n not in dic:
                dic[n] = len(res)
                res += str(n / d)
            else:
                res = res[:dic[n]] + '(' + res[dic[n] :]
                res += ')'
                break
            n = (n % d) * 10
        return res if flag == 1 else '-' + res
