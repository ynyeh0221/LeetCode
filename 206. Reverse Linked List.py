# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p1 = head
        p2 = head
        nextnode = None
        
        while p1:
            p2 = p1.next
            p1.next = nextnode
            dummy.next = p1
            nextnode = dummy.next
            p1 = p2
        return dummy.next
