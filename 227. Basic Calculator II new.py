class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = temp = num = 0
        op = '+'
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = 10 * num + int(s[i])
                    i += 1
                if op == "+" or op == "-":
                    res += temp
                    temp = num if op == "+" else -num
                elif op == "*":
                    temp *= num
                elif op == "/":
                    if temp >= 0:
                        temp /= num
                    else:
                        t = -temp
                        temp = -(t / num)
            if i < len(s) and s[i] != ' ':
                op = s[i]
            i += 1
        res += temp
        return res
