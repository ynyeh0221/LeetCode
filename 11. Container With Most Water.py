class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        res = min(height[l], height[r]) * (r-l)
        while l < r:
            res = max(res, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res
