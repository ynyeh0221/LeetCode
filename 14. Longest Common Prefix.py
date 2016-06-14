class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        res = ""
        ind = 0
        while True:
            temp = ""
            for str in strs:
                if ind == len(str):
                    return res
                if temp == "":
                    temp = str[ind]
                if str[ind] != temp:
                    return res
            res += temp
            ind += 1
