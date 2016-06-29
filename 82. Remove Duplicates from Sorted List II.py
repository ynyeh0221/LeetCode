# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1 = dummy
        p2 = head
        while p2 and p2.next:
            if p2.val == p2.next.val:
                while p2 and p2.next and p2.val == p2.next.val:
                    p2 = p2.next
                p2 = p2.next
                p1.next = p2
            else:
                p2 = p2.next
                p1 = p1.next
        return dummy.next
