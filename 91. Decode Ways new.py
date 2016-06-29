class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        T = [0 for i in xrange(len(s))]
        T[0] = 1
        if len(s) > 1:
            if int(s[0:2]) <= 26 and s[1] != '0':
                T[1] = 2
            elif (int(s[0:2]) <= 26 and s[1] == '0') or (int(s[0:2]) > 26 and s[1] != '0'):
                T[1] = 1
            else:
                return 0
        for i in xrange(2, len(s)):
            if s[i] == '0' and s[i-1] == '0':
                return 0
            elif s[i] != '0' and s[i-1] != '0':
                T[i] += T[i-1]
                if int(s[i-1:i+1]) <= 26:
                    T[i] += T[i-2]
            elif s[i] == '0' and s[i-1] != '0':
                if int(s[i-1:i+1]) <= 26:
                    T[i] += T[i-2]
                else:
                    return 0
            else:
                T[i] += T[i-1]
        return T[len(s)-1]
