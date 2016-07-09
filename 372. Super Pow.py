import collections
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        mod = 1337
        dic = collections.OrderedDict()
        times = 1
        i = a % mod
        b = int(''.join(str(j) for j in b))
        while times < b and i not in dic:
            dic[i] = times
            times += 1
            i = (i*a) % mod
        if b > times:
            period = times - dic[i]
            return dic.items()[(b - times) % period][0]
        else:
            return i
