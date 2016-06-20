# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(-1)
        lesshead = less
        notless = ListNode(-1)
        notlesshead = notless
        while head:
            if head.val < x:
                less.next = head
                head = head.next
                less = less.next
                less.next = None
            elif head.val >= x:
                notless.next = head
                head = head.next
                notless = notless.next
                notless.next = None
        less.next = notlesshead.next
        return lesshead.next
