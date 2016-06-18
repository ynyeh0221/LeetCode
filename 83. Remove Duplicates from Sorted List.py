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
        p2 = p1.next
        while p2:
            if p2.val == p1.val:
                p2 = p2.next
            else:
                self.delete(p1, p2)
                p1 = p1.next
                p2 = p2.next
        self.delete(p1, p2)
        return head
    
    def delete(self, p1, p2):
        temp = p1.next
        ptemp = temp
        p1.next = p2
        while temp != p2:
            ptemp = temp.next
            del temp
            temp = ptemp
