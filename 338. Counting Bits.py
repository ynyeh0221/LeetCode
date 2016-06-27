class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0,1,1,2,1,2,2,3]
        ind = 4
        while len(res) <= num:
            temp = res[ind:]
            ind = len(res)
            res += temp
            res += [x+1 for x in temp]
        return res[:num+1]
