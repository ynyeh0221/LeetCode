class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for i in strs:
            temp = ''.join(sorted(i))
            if temp not in dic:
                dic[temp] = []
            dic[temp] += [i]
        res = []
        for key, value in dic.items():
            res += [value]
        return res
