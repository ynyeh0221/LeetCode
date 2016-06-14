class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start<=end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            else:
                if not s[start].isalnum():
                    start += 1
                elif not s[end].isalnum():
                    end -= 1
        return True
