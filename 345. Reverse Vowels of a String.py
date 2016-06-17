class Solution(object):
    def vowel(self, a):
        if a=="a" or a=="e" or a=="i" or a=="o" or a=="u" or a=="A" or a=="E" or a=="I" or a=="O" or a=="U":
            return True
        return False
        
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if self.vowel(s[l]) and self.vowel(s[r]):
                temp=s[l]
                s[l]=s[r]
                s[r]=temp
            else:
                if self.vowel(s[l]):
                    l-=1
                if self.vowel(s[r]):
                    r+=1
            l+=1
            r-=1
        return "".join(s)
