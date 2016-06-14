import operator
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        res = []
        for pair in sorted(dic.items(), key = operator.itemgetter(1), reverse = True):
            if len(res) == k:
                break
            res += [pair[0]]
        return res
