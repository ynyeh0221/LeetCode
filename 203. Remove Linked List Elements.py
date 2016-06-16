# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = head
        pre = dummy
        
        while p:
            if p.val == val:
                pre.next = p.next
                del p
                p = pre.next
            else:
                p = p.next
                pre = pre.next
        return dummy.next
