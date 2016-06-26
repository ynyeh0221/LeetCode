# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
import sys
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.i = iterator
        self.nextnum = sys.maxint

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.nextnum == sys.maxint:
            self.nextnum = self.i.next()
            return self.nextnum
        else:
            return self.nextnum

    def next(self):
        """
        :rtype: int
        """
        if self.nextnum != sys.maxint:
            temp = self.nextnum
            self.nextnum = sys.maxint
            return temp
        else:
            if self.i.hasNext():
                return self.i.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.i.hasNext() or (not self.i.hasNext() and self.nextnum < sys.maxint) else False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
