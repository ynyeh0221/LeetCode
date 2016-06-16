# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        self.res = True
        self.preorder(p, q)
        return self.res
    
    def preorder(self, p, q):
        if p == None and q == None:
            return
        elif p == None and q:
            self.res = False
            return
        elif p and q == None:
            self.res = False
            return
        if p.val != q.val:
            self.res = False
        self.preorder(p.left, q.left)
        self.preorder(p.right, q.right)
