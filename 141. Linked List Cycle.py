# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        pslow = head
        pfast = head.next
        
        while pfast:
            pslow = pslow.next
            pfast = pfast.next
            if pfast:
                pfast = pfast.next
            if pslow == pfast:
                return True
        return False
