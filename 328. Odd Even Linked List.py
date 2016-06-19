# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(-1)
        even = ListNode(-1)
        evenhead = even
        oddhead = odd
        while head:
            odd.next = head
            head = head.next
            odd = odd.next
            odd.next = None
            if head:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
        odd.next = evenhead.next
        return oddhead.next
