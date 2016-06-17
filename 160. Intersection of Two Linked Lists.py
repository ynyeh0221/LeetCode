# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA, pB = headA, headB
        lengthA, lengthB = 0, 0
        while pA:
            lengthA += 1
            pA = pA.next
        while pB:
            lengthB += 1
            pB = pB.next
        for i in xrange(abs(lengthA - lengthB)):
            if lengthA > lengthB:
                headA = headA.next
            else:
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
