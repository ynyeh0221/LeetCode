class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
            if dic[i] == 2:
                del dic[i]
        for key, value in dic.items():
            return key
