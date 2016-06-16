class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        sum = n
        while True:
            sumlist = map(int, str(sum))
            sum = 0
            for i in sumlist:
                sum += i**2
            if sum == 1:
                return True
            if sum in dic:
                return False
            dic[sum] = 1
