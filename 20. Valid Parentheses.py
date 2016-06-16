class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack += [i]
            else:
                if (i == ')' and (len(stack) == 0 or stack[len(stack)-1] != '(')) or (i == ']' and (len(stack) == 0 or stack[len(stack)-1] != '[')) or (i == '}' and (len(stack) == 0 or stack[len(stack)-1] != '{')):
                    return False
                else:
                    stack.pop()
        return True if len(stack) == 0 else False
