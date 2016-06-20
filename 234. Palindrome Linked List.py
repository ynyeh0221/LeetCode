# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        pfast = head
        pslow = head
        while pfast:
            pfast = pfast.next
            if pfast:
                pfast = pfast.next
                pslow = pslow.next
        head2 = pslow
        
        nextnode = None
        dummy = ListNode(-1)
        while head2:
            temp = head2
            head2 = head2.next
            dummy.next = temp
            temp.next = nextnode
            nextnode = dummy.next
        head2 = dummy.next
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
