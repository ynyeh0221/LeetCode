class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start = 0
        end = len(citations)
        while start < end:
            mid = (start + end) >> 1
            if citations[mid] >= len(citations) - mid:
                end = mid
            else:
                start = mid +1
        return len(citations) - start
