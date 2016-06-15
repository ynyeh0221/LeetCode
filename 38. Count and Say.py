class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in xrange(1,n):
            temp = ""
            count = 0
            for j in xrange(len(res)):
                if j == 0:
                    count +=1
                else:
                    if res[j] != res[j-1]:
                        temp += str(count) + res[j-1]
                        count = 1
                    else:
                        count += 1
            temp += str(count) + res[len(res)-1]
            res = temp
        return res
