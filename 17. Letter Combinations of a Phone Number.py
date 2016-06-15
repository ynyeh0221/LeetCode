class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        buttons = [[],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
        self.res = []
        self.DFS(buttons, digits, [])
        return self.res
        
    def DFS(self, buttons, digits, path):
        if len(path) == len(digits):
            self.res += [''.join(path)]
            return
        for i in xrange(len(digits)):
            if len(path) == i:
                for j in buttons[ord(digits[i]) - ord('0')]:
                    path += [j]
                    self.DFS(buttons, digits, path)
                    path.pop()
