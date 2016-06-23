# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1, p2 = dummy, head
        while n > 0:
            p2 = p2.next
            n -= 1
        while p2:
            p1 = p1.next
            p2 = p2.next
        if not p1.next:
            p1.next = None
        else:
            p1.next = p1.next.next
        return dummy.next
