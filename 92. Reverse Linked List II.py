# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        rbegin = None
        rend = None
        nextnode = None
        for i in xrange(m-1):
            p1 = p1.next
        p2 = p1.next
        for i in xrange(n-m+1):
            rend = p2
            p2 = p2.next
            rend.next = nextnode
            if nextnode == None:
                rbegin = rend
            nextnode = rend
        p1.next = rend
        rbegin.next = p2
        return dummy.next
