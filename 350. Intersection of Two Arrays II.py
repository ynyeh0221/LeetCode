class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res=[]
        i=0
        while i<len(nums1):
            if len(nums2)>0:
                if nums1[i] in nums2:
                    res+=[nums1[i]]
                    nums2.pop(nums2.index(nums1[i]))
                    nums1.pop(i)
                else:
                    i+=1
            else:
                break
        return res
