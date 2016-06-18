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
        if not head: return
        p1 = head
        while p1.next:
            if p1.val == p1.next.val:
                p1.next = p1.next.next
            else:
                p1 = p1.next
        return head
