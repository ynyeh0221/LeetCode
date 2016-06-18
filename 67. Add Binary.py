class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        self.res = ""
        self.carry = 0
        a, b = a[::-1], b[::-1]
        for i in xrange(max(len(a), len(b))):
            if i < len(a) and i < len(b):
                self.add(a[i], b[i])
            elif i < len(a) and i>= len(b):
                self.add(a[i], 0)
            elif i < len(b) and i>= len(a):
                self.add(0, b[i])
        if self.carry == 1:
            self.res = str(self.carry) + self.res
        return self.res
        
    def add(self, a, b):
        temp = int(a) + int(b) + self.carry
        if temp >= 2:
            self.res = str(temp - 2) + self.res
            self.carry = 1
        else:
            self.res = str(temp) + self.res
            self.carry = 0
