class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in xrange(len(digits)-1, -1, -1):
            if digits[i] + carry >= 10:
                digits[i] = digits[i] + carry -10
                carry = 1
            else:
                digits[i] = digits[i] + carry
                carry = 0
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits
