class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic_s = {}
        dic_t = {}
        for i,j in zip(s, t):
            if i not in dic_s and j not in dic_t:
                dic_s[i] = j
                dic_t[j] = i
            elif (i in dic_s and j not in dic_t) or (i not in dic_s and j in dic_t):
                return False
            else:
                if dic_s[i] != j or dic_t[j] != i:
                    return False
        return True
