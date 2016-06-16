class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x / 10 == 0:
            return True
        if x % 10==0:
            return False
        temp = 0
        while x > 0:
            temp = temp * 10 + (x % 10) 
            if temp == x or temp == x / 10:
                return True
            x /= 10
        return False
