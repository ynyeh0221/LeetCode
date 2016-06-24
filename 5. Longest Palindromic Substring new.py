class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=''
        if len(s) > 0:
            res = s[0]
        for i in xrange(len(s)):
            p=self.palin(s, i, i)
            if len(p)>len(res):
                res=p
            p=self.palin(s, i, i+1)
            if len(p)>len(res):
                res=p
        return res
                    
    def palin(self, s, begin, end):
        while begin>=0 and end<len(s) and s[begin]==s[end]:
            begin-=1
            end+=1
        return s[begin+1:end]
