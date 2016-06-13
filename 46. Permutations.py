class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res=[]
        self.DFS([], nums)
        return self.res
    
    def DFS(self, path, nums):
        if len(path)==len(nums):
            self.res+=[path[:]]
            return
        for i in xrange(len(nums)):
            if nums[i] in path:
                continue
            path+=[nums[i]]
            self.DFS(path, nums)
            path.pop()
