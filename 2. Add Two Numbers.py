# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        while l1 and l2:
            temp = ListNode(l1.val + l2.val + carry) if l1.val + l2.val + carry < 10 else ListNode(l1.val + l2.val + carry - 10)
            carry = 0 if l1.val + l2.val + carry < 10 else 1
            p.next = temp
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp = ListNode(l1.val + carry) if l1.val + carry < 10 else ListNode(l1.val + carry - 10)
            carry = 0 if l1.val + carry < 10 else 1
            p.next = temp
            p = p.next
            l1 = l1.next
        while l2:
            temp = ListNode(l2.val + carry) if l2.val + carry < 10 else ListNode(l2.val + carry - 10)
            carry = 0 if l2.val + carry < 10 else 1
            p.next = temp
            p = p.next
            l2 = l2.next
        if carry == 1:
            temp = ListNode(carry)
            p.next = temp
        return dummy.next
