# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.build(head, None)
        
    def build(self, left, right):
        if left == right:
            return None
        mid = self.findmid(left, right)
        root = TreeNode(mid.val)
        root.left = self.build(left, mid)
        root.right = self.build(mid.next, right)
        return root
    
    def findmid(self, left, right):
        p1 = left
        p2 = left
        while p2 != right:
            p2 = p2.next
            if p2 != right:
                p2 = p2.next
                p1 = p1.next
        return p1
