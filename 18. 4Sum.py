# timeout

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums=sorted(nums)
        res=[]
        i=0
        while i < n:
            j=i+1
            while j < n:
                k=j+1
                l=n-1
                while l>k:
                    if nums[i]+nums[k]+nums[j]+nums[l] == target:
                        res+=[[nums[i], nums[j], nums[k], nums[l]]]
                        k+=1
                        l-=1
                        while k<j and nums[k]==nums[k-1]:
                            k+=1
                        while l>j and l<n-1 and nums[l]==nums[l+1]:
                            l-=1
                    elif nums[i]+nums[k]+nums[j]+nums[l] > target:
                        l-=1
                        while l>j and l<n-1 and nums[l]==nums[l+1]:
                            l-=1
                    else:
                        k+=1
                        while k<j and nums[k]==nums[k-1]:
                            k+=1
                j+=1
                while j<n and nums[j]==nums[j-1]:
                    j+=1
            i+=1
            while i<n and nums[i]==nums[i-1]:
                i+=1
        return res
