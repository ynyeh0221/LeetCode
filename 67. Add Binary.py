class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        carry = 0
        a, b = a[::-1], b[::-1]
        for i in xrange(max(len(a), len(b))):
            if i < len(a) and i < len(b):
                temp = int(a[i]) + int(b[i]) + carry
                if temp >= 2:
                    res = str(temp - 2) + res
                    carry = 1
                else:
                    res = str(temp) + res
                    carry = 0
            elif i < len(a) and i>= len(b):
                temp = int(a[i]) + carry
                if temp >= 2:
                    res = str(temp - 2) + res
                    carry = 1
                else:
                    res = str(temp) + res
                    carry = 0
            elif i < len(b) and i>= len(a):
                temp = int(b[i]) + carry
                if temp >= 2:
                    res = str(temp - 2) + res
                    carry = 1
                else:
                    res = str(temp) + res
                    carry = 0
        if carry == 1:
            res = str(carry) + res
        return res
