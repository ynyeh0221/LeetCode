# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        length = 0
        while p and p.next:
            length += 1
            p = p.next
        length += 1
        k = k % length
        p.next = head
        for i in xrange(length - k):
            p = p.next
        newhead = p.next
        p.next = None
        return newhead
