class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False
