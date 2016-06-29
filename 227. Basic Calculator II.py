# timeout

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i <len(s):
            if s[i] == u'+':
                s = s[:i] + " + " +s[i+1:]
                i += 2
            elif s[i] == u'-':
                s = s[:i] + " - " +s[i+1:]
                i += 2
            elif s[i] == u'*':
                s = s[:i] + " * " +s[i+1:]
                i += 2
            elif s[i] == u'/':
                s = s[:i] + " / " +s[i+1:]
                i += 2
            i += 1
        s = s.split(' ')
        num = []
        ope = []
        i = 0
        while i < len(s):
            if s[i] == u"*":
                n1 = num.pop()
                while s[i+1] == ' ' or s[i+1] == '':
                    i += 1
                num += [n1 * int(s[i+1])]
                i += 1
            elif s[i] == u"/":
                n1 = num.pop()
                while s[i+1] == ' ' or s[i+1] == '':
                    i += 1
                num += [n1 / int(s[i+1])]
                i += 1
            elif s[i] == u'+' or s[i] == u'-':
                ope += [s[i]]
            elif s[i] != ' ' and s[i] != '':
                num += [int(s[i])]
            i += 1
        res = num.pop(0)
        while num:
            n2 = num.pop(0)
            operator = ope.pop(0)
            if operator == u'+':
                res += n2
            else:
                res -= n2
        return res
