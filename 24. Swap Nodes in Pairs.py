# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(-1)
        p = dummy
        p1 = head
        p2 = p1.next
        while p1 and p2:
            p.next = p2
            p1.next = p2.next
            p2.next = p1
            p = p1
            p1 = p1.next
            if p1:
                p2 = p1.next
        return dummy.next
